import json
import time

from google import genai
from google.genai.errors import ServerError

from config import GEMINI_API_KEY


class GeminiService:

    def __init__(self):

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

        # Faster and much less likely to return 503
        self.model = "gemini-3.5-flash-lite"

    def generate(self, prompt):

        for attempt in range(5):

            try:

                response = self.client.models.generate_content(
                    model=self.model,
                    contents=prompt
                )

                return response.text

            except ServerError as e:

                wait = min((2 ** attempt) * 5, 60)

                print(f"\nGemini server busy (Attempt {attempt + 1}/5)")
                print(f"Retrying in {wait} seconds...\n")

                time.sleep(wait)

            except Exception as e:

                print("\nUnexpected Error")
                raise e

        raise RuntimeError(
            "Gemini API unavailable after multiple retries."
        )

    def generate_json(self, prompt):

        for attempt in range(3):

            response = self.generate(prompt)

            if not response:

                continue

            response = response.replace("```json", "")
            response = response.replace("```", "")
            response = response.strip()

            try:

                return json.loads(response)

            except json.JSONDecodeError as e:

                print(f"\nInvalid JSON (Attempt {attempt + 1})")
                print(e)

        raise ValueError(
            "Gemini failed to generate valid JSON."
        )