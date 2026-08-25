import hashlib
import os
import time
from pathlib import Path
import chromadb
from google import genai
from google.genai.errors import ClientError
from langchain_text_splitters import RecursiveCharacterTextSplitter
from _0_init_config import config_settings
from _1_api_key_manager import APIKey


class Error429(Exception):
    pass


class LocalRAGPipeline:
    def __init__(self, db_path: str = None, collection_name: str = "gcp_docs"):
        if db_path is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(base_dir, "chroma_db")

        api_keys = config_settings.get("api_keys")

        if not api_keys:
            raise ValueError("You need to setup api_keys first!")

        self.api_keys = api_keys
        self.current_key_index = 0
        self.key_manager = APIKey(api_keys)

        # initializing Gemini Client with the 1st available API Key
        self._init_client()

        # initializing the vector DB
        self.chroma_client = chromadb.PersistentClient(path=db_path)
        self.collection = self.chroma_client.get_or_create_collection(
            name=collection_name
        )

    def _init_client(self):
        # initializing Gemini Client with the current API Key
        current_key = self.key_manager.get_current_key()
        current_key_num = self.key_manager.current_key_index + 1
        total = len(self.key_manager.api_keys)

        print(f"Using API Key #{current_key_num} (of {total})")
        self.ai_client = genai.Client(api_key=current_key)

    def parse_error(self, e):
        try:
            error_msg = getattr(e, "details", "") or str(e)
            quota_id = error_msg["error"]["details"][1]["violations"][0]["quotaId"]
            quota_value = error_msg["error"]["details"][1]["violations"][0][
                "quotaValue"
            ]
            err_msg = f"Resource exhasted at {quota_id} ({quota_value})"
            # return {"quota_id": quota_id, "quota_value": quota_value}
        except IndexError:
            err_msg = e.message
        return err_msg

    def reset_collection(self):
        self.chroma_client.delete_collection(self.collection.name)
        self.collection = self.chroma_client.get_or_create_collection(
            name=self.collection.name
        )
        print("The DB has been reset!")

    def _get_embedding(self, text: str) -> list[float]:
        # retrieving vectors via gemini-embedding-001 model
        while True:
            try:
                response = self.ai_client.models.embed_content(
                    model="gemini-embedding-001",
                    contents=text,
                )
                return response.embeddings[0].values
            except ClientError as e:
                error_msg = str(e)

                # checking if a quota for requests has been reached
                if "429" in error_msg:
                    err_msg = self.parse_error(e)

                    # if it's a daily quota - stopping
                    if "perday" in error_msg.lower():
                        # re-initializing Gemini Client with the next API Key
                        if self.key_manager.rotate_key():
                            self._init_client()
                            continue
                        else:
                            raise Error429(f"{err_msg} for all API keys!")

                    # if it's a minute quota - timeout
                    elif "perminute" in error_msg.lower():
                        time.sleep(60)
                        print(f"{err_msg}\nWaiting for 60 seconds...")

                else:
                    # if any other error
                    raise e

    def chunk_text(
        self, text: str, chunk_size: int = 1000, overlap: int = 200
    ) -> list[str]:

        # initializing the logical text splitter
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=overlap,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )

        # splitting into strings
        chunks = splitter.split_text(text)

        return chunks

    def ingest_document(self, doc_id: str, text: str, metadata: dict = None):
        # splitting the texts into chunks, generating the vectors and saving them in ChromaDB
        chunks = self.chunk_text(text)

        for idx, chunk in enumerate(chunks):
            chunk_id = f"{doc_id}_chunk_{idx}"
            vector = self._get_embedding(chunk)

            chunk_metadata = metadata or {}
            chunk_metadata["chunk_index"] = idx

            self.collection.add(
                ids=[chunk_id],
                embeddings=[vector],
                documents=[chunk],
                metadatas=[chunk_metadata],
            )
        print(f"Loaded {len(chunks)} chunks for the document: {doc_id}")

    def search(self, query: str, top_k: int = 3) -> list[dict]:
        # semantic search of the closest vectors
        try:
            query_vector = self._get_embedding(query)

            results = self.collection.query(
                query_embeddings=[query_vector], n_results=top_k
            )

            formatted_results = []
            if results["documents"]:
                for doc, meta, dist in zip(
                    results["documents"][0],
                    results["metadatas"][0],
                    results["distances"][0],
                ):
                    formatted_results.append(
                        {"content": doc, "metadata": meta, "distance": dist}
                    )

            return formatted_results

        except Error429:
            print(
                "Your daily limit has reached.\nCome back tomorrow. Or not. Whatever."
            )
            return []

        except ClientError as e:
            print(f"\nAPI Error during search: {e}")

            return []

    def process_files(self, input_dir, RESET_DB=False):
        docs_dir = Path(input_dir)

        if RESET_DB:
            self.reset_collection()

        if docs_dir.exists():
            print("Starting to index Google Cloud documentation...\n")

            # reading the metadata to check if the files have been already indexed
            existing_records = self.collection.get(include=["metadatas"])
            processed_files = {}

            if existing_records and existing_records["metadatas"]:
                for meta in existing_records["metadatas"]:
                    if meta and "source_file" in meta and "file_hash" in meta:
                        processed_files[meta["source_file"]] = meta["file_hash"]

            print(f"Already existing in the DB: {len(processed_files)} files in total")

            # # indexing the remaining files recursively
            # for file_path in docs_dir.rglob("*.md"):
            #     if file_path.name in processed_files:
            #         print(f"Skipping {file_path.name} (already indexed)")
            #         continue

            # indexing the files recursively
            for file_path in docs_dir.rglob("*.md"):
                with open(file_path, "rb") as f:
                    content_bytes = f.read()
                    current_hash = hashlib.md5(content_bytes).hexdigest()

                filename = file_path.name

                # checking the hash sums of the input files
                if filename in processed_files:
                    if processed_files[filename] == current_hash:
                        print(f"Skipping {filename} (already indexed and unchanged)")
                        continue
                    else:
                        print(f"File {filename} has changed. Updating in DB...")
                        # deleting old chunks before writing new ones
                        self.collection.delete(where={"source_file": filename})
                else:
                    print(f"Indexing new file: {filename}")

                # decoding the raw bytes of the content
                content = content_bytes.decode("utf-8")
                doc_id = file_path.stem

                # defining the file structure for use in DB as metadata
                folder_name = file_path.parent.name
                product_category = (
                    "general" if folder_name == docs_dir.name else folder_name
                )

                # processing the files
                self.ingest_document(
                    doc_id=doc_id,
                    text=content,
                    metadata={
                        "source_file": file_path.name,
                        "gcp_product": product_category,
                        "file_hash": current_hash,
                    },
                )
            print("\nAll the files have been indexed successfully!")
        else:
            print(f"The dir {docs_dir} wasn't found.")


if __name__ == "__main__":
    docs = "gcp_documentation"
    rag = LocalRAGPipeline()

    rag.process_files(docs)

    # # testing semantic search (should be working even if file indexing was stopped)
    # test_query = "How are buckets and storage tiers structured in object storage?"
    # print(f"\nPrompt: '{test_query}'")
    #
    # search_results = rag.search(query=test_query, top_k=5)
    # print("\n--- The following relevant chunks were found ---")
    #
    # for res in search_results:
    #     product = res["metadata"].get("gcp_product", "unknown")
    #     print(
    #         f"Source: {res['metadata']['source_file']} | GCP Product: {product} | (distance: {res['distance']:.4f})"
    #     )
    #     print(f"The chunk content:\n{res['content']}\n" + "-" * 40)
