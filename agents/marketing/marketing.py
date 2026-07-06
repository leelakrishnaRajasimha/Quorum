from core.llm.llm_service import LLMService
from core.models.models import StartupIdea, AgentResponse, Vote
from tools.scoring.confidence import ConfidenceEngine

class MarketingAgent:

    def __init__(self, provider="gemini"):
        self.name = "Marketing"
        self.confidence_engine = ConfidenceEngine()
        self.llm = LLMService(provider)

    def analyze(self, idea: StartupIdea, board_context: str) -> AgentResponse:

        prompt = f"""
You are the Chief Marketing Officer (CMO) of Quorum.

Startup Title:
{idea.title}

Description:
{idea.description}

Target Users:
{idea.target_users}

Previous Executive Discussion:
{board_context}

Read the previous discussion.

Do NOT repeat Research, Finance, Product or Architecture.

Build a marketing strategy based on their conclusions.

Return ONLY:

1. Customer Persona
2. Go-To-Market Strategy
3. Acquisition Channels
4. Brand Positioning
5. Launch Plan
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

Keep it under 300 words.
"""

        response = self.llm.generate(prompt)

        if response.startswith("ERROR"):

            return AgentResponse(
                agent_name=self.name,
                finding="Marketing analysis could not be completed.",
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