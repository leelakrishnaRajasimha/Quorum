from core.llm.llm_service import LLMService


class FinancialProjection:

    def __init__(self, provider="gemini"):

        self.llm = LLMService(provider)

    def generate(self, idea, board_summary):

        prompt = f"""
You are an experienced startup CFO and Venture Capital advisor.

Startup

Title:
{idea.title}

Description:
{idea.description}

Budget:
{idea.budget}

Board Discussion:
{board_summary}

Estimate realistic financial projections.

Return ONLY:

Estimated MVP Cost

Monthly Burn Rate

Estimated Break-even Time

Suggested Pricing Model

3-Year Revenue Potential

Funding Recommendation

Keep estimates realistic.

If the startup idea is weak, clearly state that.

Do not inflate numbers.
"""

        return self.llm.generate(prompt)