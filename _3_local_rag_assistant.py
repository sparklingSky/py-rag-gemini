from _0_init_config import config_settings
from _2_local_rag_pipeline import LocalRAGPipeline
from google.genai import types
from pydantic import BaseModel, Field


class RAGResponse(BaseModel):
    answer: str = Field()
    context_used: bool = Field(
        description="Set True if there's a response based on the context. Set False if used a fallback message"
    )


class RAGAssistant:
    def __init__(self):
        # initializing the search pipeline
        self.retriever = LocalRAGPipeline()
        self.model = config_settings.get("model_id")
        self.system_instruction = config_settings["system_instruction"]
        self.fallback_message = config_settings["fallback_message"]
        self.retrieved_chunks = None

        # reusing Gemini client instance (including its current API key state) from retriever
        self.ai_client = self.retriever.ai_client

    def ask(self, user_query: str) -> str:
        # serahcing for the relevant chunks
        print(f"Searching for context for: '{user_query}'...")
        self.retrieved_chunks = self.retriever.search(query=user_query, top_k=5)

        if not self.retrieved_chunks:
            return "I couldn't find any relevant information in the documentation."

        # creating the context with the found chunks
        context_parts = []
        for i, res in enumerate(self.retrieved_chunks):
            product = res["metadata"].get("gcp_product", "unknown")
            context_parts.append(
                f"Document {i + 1} (Product: {product}) \n{res['content']}"
            )

        context_string = "\n\n".join(context_parts)
        # print(context_string)

        # creating a prompt
        prompt = (
            f"CONTEXT:\n{context_string}\n\nUSER QUESTION:\n{user_query}\n\nANSWER:"
        )
        # generating an answer
        print("Generating answer...\n")
        response = self.ai_client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=self.system_instruction,
                temperature=0.0,
                response_mime_type="application/json",
                response_schema=RAGResponse,
            ),
        )

        return response


if __name__ == "__main__":
    assistant = RAGAssistant()

    # question = "List the main product categories in Google Cloud"
    question = "Which AI and ML products does Google Cloud include?"
    # question = "What is Cloud Run?"
    # question = "Which predefined permissions does Data Scientist role have?"
    # question = "What is the difference between BigQuery and SAP HANA?"

    response = assistant.ask(question).text

    print("-" * 50)
    print(response)
    print("-" * 50)
