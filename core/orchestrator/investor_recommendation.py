from core.llm.llm_service import LLMService


class InvestorRecommendation:

    def __init__(self, provider="gemini"):

        self.llm = LLMService(provider)

    def generate(self, idea, board_summary):

        prompt = f"""
You are a senior Venture Capital partner.

Startup

Title:
{idea.title}

Description:
{idea.description}

Budget:
{idea.budget}

Executive Board Analysis:
{board_summary}

Decide whether you would invest.

Return ONLY:

Investment Decision
(Invest / Do Not Invest)

Investment Readiness Score
(0-100)

Reasons

Top Strengths

Major Risks

Suggested Improvements

Be brutally honest.

Do not inflate scores.

If the startup is weak,
recommend against investing.
"""

        return self.llm.generate(prompt)