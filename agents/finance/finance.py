from core.llm.llm_service import LLMService
from core.models.models import StartupIdea, AgentResponse, Vote
from tools.scoring.confidence import ConfidenceEngine

class FinanceAgent:

    def __init__(self, provider="gemini"):
        self.name = "Finance"
        self.confidence_engine = ConfidenceEngine()
        self.llm = LLMService(provider)

    def analyze(self, idea: StartupIdea, board_context: str) -> AgentResponse:

        prompt = f"""
You are the Chief Financial Officer (CFO) of Quorum.

Your responsibility is to evaluate ONLY the financial viability of the startup.

Startup Title:
{idea.title}

Description:
{idea.description}

Budget:
{idea.budget}

Previous Board Discussion:
{board_context}

Carefully review the previous executives' findings before making your decision.

Do NOT repeat previous points.

Build upon the existing discussion.

If another executive's recommendation increases cost, risk, or revenue, mention it.

Return ONLY:

1. Estimated MVP Development Cost
2. Monthly Operational Cost
3. Suggested Pricing Model
4. Revenue Potential
5. Biggest Financial Risk
6. Recommendation

If you disagree with a previous executive,
clearly explain why.

If you agree,
state what additional evidence supports that decision.

Do not blindly agree.

Act as an independent executive.

Previous Executive Discussion:

{board_context}

You are an independent executive.

Carefully review the previous executives' opinions before making your decision.

If you agree with another executive,
briefly explain why.

If you disagree,
explain your reasoning professionally.

Avoid repeating previous analysis unless it is necessary.

Provide new insights from your own executive perspective.

Your recommendation must be independent.

Return only the requested output.

Keep it under 250 words.
"""

        response = self.llm.generate(prompt)

        if response.startswith("ERROR"):

            return AgentResponse(
                agent_name=self.name,
                finding="Finance analysis could not be completed.",
                recommendation="Retry",
                confidence=0,
                concerns=["LLM service unavailable"],
                vote=Vote.MODIFY
                )

        return AgentResponse(
            agent_name=self.name,
            finding=response,
            recommendation="Proceed",
            confidence=self.confidence_engine.calculate(response),
            concerns=[],
            vote=Vote.APPROVE
        )