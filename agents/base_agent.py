from services.gemini_service import GeminiService


class BaseAgent:

    def __init__(self):

        self.llm = GeminiService()

    def generate(self, prompt):

        return self.llm.generate(prompt)

    def generate_json(self, prompt):

        return self.llm.generate_json(prompt)