from core.llm.llm_service import LLMService
from core.models.models import StartupIdea, AgentResponse, Vote
from tools.scoring.confidence import ConfidenceEngine

class ArchitectureAgent:

    def __init__(self, provider="gemini"):
        self.name = "Architecture"
        self.confidence_engine = ConfidenceEngine()
        self.llm = LLMService(provider)

    def analyze(self, idea: StartupIdea, board_context: str) -> AgentResponse:

        prompt = f"""
You are the Chief Technology Officer (CTO) of Quorum.

Startup Title:
{idea.title}

Description:
{idea.description}

Budget:
{idea.budget}

Timeline:
{idea.timeline}

Previous Executive Discussion:
{board_context}

Read everything discussed before.

Do NOT repeat Research, Finance or Product.

Use their findings to design the technical solution.

Return ONLY:

1. Tech Stack
2. System Architecture
3. AI Components
4. Scalability
5. Development Plan
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

Keep it under 350 words.
"""

        response = self.llm.generate(prompt)

        if response.startswith("ERROR"):

            return AgentResponse(
                agent_name=self.name,
                finding="Architecture analysis could not be completed.",
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