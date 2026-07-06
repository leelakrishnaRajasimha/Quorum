from core.llm.llm_service import LLMService
from core.models.models import StartupIdea, AgentResponse, Vote
from tools.scoring.confidence import ConfidenceEngine

class ProductAgent:

    def __init__(self, provider="gemini"):
        self.name = "Product"
        self.confidence_engine = ConfidenceEngine()
        self.llm = LLMService(provider)

    def analyze(self, idea: StartupIdea, board_context: str) -> AgentResponse:

        prompt = f"""
You are the Chief Product Officer (CPO) of Quorum.

Your responsibility is to design the best product strategy.

Startup Title:
{idea.title}

Description:
{idea.description}

Target Users:
{idea.target_users}

Previous Board Discussion:
{board_context}

Read all previous executive discussions.

Do NOT repeat what Research or Finance already said.

Instead:

- Build on previous decisions.
- Design the product accordingly.
- If Finance suggested budget limitations, adapt the MVP.
- If Research identified opportunities, convert them into product features.

Return ONLY:

1. Core Problem
2. MVP Features
3. Premium Features
4. User Journey
5. Product Differentiation
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

Keep it under 400 words.
"""

        response = self.llm.generate(prompt)

        if response.startswith("ERROR"):

            return AgentResponse(
                agent_name=self.name,
                finding="Product analysis could not be completed.",
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