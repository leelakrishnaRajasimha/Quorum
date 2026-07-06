from core.llm.llm_service import LLMService


class SuccessPredictor:

    def __init__(self, provider="gemini"):

        self.llm = LLMService(provider)

    def predict(self, idea, board_summary):

        prompt = f"""
You are an experienced Venture Capital partner.

Startup:

Title:
{idea.title}

Description:
{idea.description}

Budget:
{idea.budget}

Board Analysis:
{board_summary}

Estimate the startup's probability of success.

Return ONLY:

Startup Success Probability:
(number between 0 and 100)

Reasons:
- ...
- ...
- ...

Be brutally honest.

If the startup is weak, give a low score.

Do not inflate numbers.
"""

        return self.llm.generate(prompt)