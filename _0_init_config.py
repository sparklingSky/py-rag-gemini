import keyring

FALLBACK_MSG = "I don't have enough information to answer that based on the provided documentation."

config_settings = {
    # "model_id": "gemini-3-flash-preview",
    # "model_id": "gemini-flash-latest",
    # "model_id": "gemini-2.5-flash",
    # "model_id": "gemini-1.5-flash",
    "model_id": "gemini-flash-lite-latest",  # at least stable
    "system_instruction": f"""You are a helpful Senior Google Cloud Platform Architect assistant. 
                            Use ONLY the following context to answer the user's question. 
                            If the answer is not contained in the context, the 'answer' field MUST be 
                            EXACTLY this phrase: '{FALLBACK_MSG}'""",
    "fallback_message": FALLBACK_MSG,
    "judge_system_instruction": """You are an impartial and strict AI QA Engineer evaluating a RAG system.
            Evaluate the answer provided by the RAG system based on the user's question and the expected behavior.
            Rate the answer from 1 to 5 based on accuracy, relevance, and alignment with the expected behavior.
            1 - Completely wrong or hallucinates.
            5 - Perfect, accurate, and follows instructions.
            Return ONLY a valid JSON object in this exact format:
            {"score": <int>, "reasoning": "<string>"}""",
    "response_mime_type": "application/json",
    "api_keys": {
        0: {"api_key": keyring.get_password("gemini_api_key", "api_user1")},
        1: {"api_key": keyring.get_password("gemini_api_key", "api_user2")},
        2: {"api_key": keyring.get_password("gemini_api_key", "api_user3")},
        3: {"api_key": keyring.get_password("gemini_api_key", "api_user4")},
        4: {"api_key": keyring.get_password("gemini_api_key", "api_user5")},

    },
}
