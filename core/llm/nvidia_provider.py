import os
import time
from openai import OpenAI, timeout

from core.llm.base_provider import BaseProvider


class NvidiaProvider(BaseProvider):

    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv("NVIDIA_API_KEY"),
            base_url="https://integrate.api.nvidia.com/v1",
            timeout=30
        )

    def generate_text(self, prompt):

        retries = 3

        for attempt in range(retries):

            try:
                
                response = self.client.chat.completions.create(
                    model="meta/llama-3.3-70b-instruct",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    temperature=0.3
                )

                return response.choices[0].message.content

            except Exception as e:

                print(f"NVIDIA Error: {e}")

                if attempt < retries - 1:
                    time.sleep(2)

        return "ERROR: Unable to generate AI response."