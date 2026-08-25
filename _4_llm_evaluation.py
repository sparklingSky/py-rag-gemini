import json

from _0_init_config import config_settings
from _3_local_rag_assistant import RAGAssistant
from google.genai import types


class RAGEvaluator:
    def __init__(self):
        # initializing the RAG agent to be evaluated
        self.assistant = RAGAssistant()
        self.model = config_settings.get("model_id")
        self.judge_system_instruction = config_settings["judge_system_instruction"]
        self.response_mime_type = config_settings.get("response_mime_type")

        # initializing the same RAG agent as a "judge" to evaluate
        self.judge_client = self.assistant.ai_client

    def judge_dredd(self, question: str, answer: str, expected_behavior: str) -> dict:
        judge_prompt = f"""USER QUESTION: {question}
                            EXPECTED BEHAVIOR: {expected_behavior}
                            RAG ANSWER TO EVALUATE: {answer}"""

        # preparing an evaluation response as JSON
        response = self.judge_client.models.generate_content(
            model=self.model,
            contents=judge_prompt,
            config=types.GenerateContentConfig(
                response_mime_type=self.response_mime_type,
                system_instruction=self.judge_system_instruction,
                temperature=0.0,
            ),
        )

        # json => dict
        return json.loads(response.text)

    def run_lethal_force(self, test_cases: list[dict]) -> None:
        print("Starting LLM Evaluations...\n" + "=" * 50)
        total_score = 0

        for i, test in enumerate(test_cases):
            print(f"Test Case {i + 1}: {test['question']}")

            # getting answers from RAG Assistant
            rag_response = json.loads(self.assistant.ask(test["question"]).text)
            rag_answer = rag_response["answer"]
            print(f"RAG Output: {rag_answer[:100]}...\n")
            # print(f"RAG Output: {rag_answer}...\n")

            # evaluating the answers from RAG Assistant by RAG Evaluator
            eval_result = self.judge_dredd(
                test["question"], rag_answer, test["expected_behavior"]
            )

            print(f"Score: {eval_result['score']}/5")
            print(f"Reasoning: {eval_result['reasoning']}")
            print("-" * 50)

            total_score += eval_result["score"]

        avg_score = total_score / len(test_cases)
        print(f"Average System Score: {avg_score:.2f} / 5.0")


if __name__ == "__main__":
    TEST_CASES = [
        {
            "question": "How are buckets and storage classes structured in object storage?",
            "expected_behavior": "Should explain buckets, projects, and storage classes based on GCP docs.",
        },
        {
            "question": "Which permissions can have Data Scientist role?",
            "expected_behavior": "Should provide the descriptive list of the available permissions.",
        },
        {
            "question": "What is Cloud Run?",
            "expected_behavior": "Should explain that it is a managed compute platform for containerized applications.",
        },
        {
            "question": "What is the difference between BigQuery and SAP HANA?",
            "expected_behavior": "Should decline to answer and state there is not enough information in the context.",
        },
    ]

    evaluator = RAGEvaluator()
    evaluator.run_lethal_force(TEST_CASES)
