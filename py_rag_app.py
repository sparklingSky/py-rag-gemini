import json
import time

import streamlit as st
from _0_init_config import config_settings
from _3_local_rag_assistant import RAGAssistant

st.title("GCP Architecture Assistant")
st.set_page_config(page_title="GCP Architecture Assistant", page_icon="☁️")
model_id = config_settings.get("model_id")

# initializing the chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


def clear_chat():
    # resetting the chat history
    st.session_state.messages = []
    # resetting the pill selection if it was selected
    if "pill_key" in st.session_state:
        st.session_state.pill_key = None


# extracting the chat details
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
        # extracting the chunks info
        if "chunks" in msg:
            with st.expander("View Retrieved Context Sources"):
                for i, doc in enumerate(msg["chunks"], 1):
                    st.markdown(f"**Chunk {i}:**")
                    st.caption(doc)

# predefined prompts
selected_pill = st.pills(
    "Choose a quick prompt:",
    [
        "Which AI and ML products does Google Cloud include?",
        "What is BigQuery?",
        "How can I create a VM machine?",
        "Which permissions does Data Scientist role have?",
        "What is the difference between BigQuery and SAP HANA?",
    ],
    key="pill_key",
)

prompt = st.chat_input("Ask a question about GCP:")

# identifying a new query
user_query = None
if prompt:
    user_query = prompt
elif selected_pill:
    # preventing a query from repeating in case View Retrieved Context Sources is expanded or another action done
    if (
        not st.session_state.messages
        or st.session_state.messages[-2]["content"] != selected_pill
    ):
        user_query = selected_pill

# processing a new query
if user_query:
    # showing the user's query and adding it to the history
    st.chat_message("user").write(user_query)
    st.session_state.messages.append({"role": "user", "content": user_query})

    # initializing RAG Assistant instance
    assistant = RAGAssistant()

    # processing a new query itself
    with st.spinner("Searching knowledge base and generating answer..."):
        response = assistant.ask(user_query)
        response_data = json.loads(response.text)

        retrieved_chunks = assistant.retrieved_chunks

    # generating the response for a live typewriter effect
    def text_generator(text):
        for word in text.split(" "):
            yield word + " "
            time.sleep(0.05)

    # rendering the response
    with st.chat_message("assistant"):
        # option 1 - with live typewriter effect
        st.write_stream(text_generator(response_data["answer"]))
        # option 2 - instant showing the full response
        # st.write(answer)

        if response_data["context_used"] is True:
            with st.expander("View Retrieved Context Sources"):
                for i, doc in enumerate(retrieved_chunks, 1):
                    st.markdown(f"**Chunk {i}:**")
                    st.caption(doc)

    # saving the current response and chunks to the history to be fetched and rendered in case there is another query
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response_data["answer"],
            "chunks": retrieved_chunks,
        }
    )

# footer for Clear Chat button and info
st.divider()

# showing the button only in case there's a chat history
if len(st.session_state.messages) > 0:
    st.button("Clear Chat", on_click=clear_chat)

st.caption(f"**Connected Model:** `{model_id}` | **Database:** `ChromaDB`")
