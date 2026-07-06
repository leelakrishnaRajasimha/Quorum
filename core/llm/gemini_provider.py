from google import genai
from dotenv import load_dotenv
import os
import time

from core.llm.base_provider import BaseProvider

load_dotenv()


class GeminiProvider(BaseProvider):

    def __init__(self):

        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

    def generate_text(self, prompt):

        retries = 3

        for attempt in range(retries):

            try:

                response = self.client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )

                return response.text

            except Exception as e:

                print(f"LLM Error: {e}")

                if attempt < retries - 1:
                    print("Retrying...")
                    time.sleep(2)

        return "ERROR: Unable to generate AI response."