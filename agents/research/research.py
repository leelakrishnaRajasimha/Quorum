from core.llm.llm_service import LLMService

from core.models.models import StartupIdea, AgentResponse, Vote
from tools.scoring.confidence import ConfidenceEngine

class ResearchAgent:

    def __init__(self, provider="gemini"):
        self.name = "Research"
        self.confidence_engine = ConfidenceEngine()
        self.llm = LLMService(provider)

    def analyze(self, idea: StartupIdea, board_context: str) -> AgentResponse:

        prompt = f"""
You are the Chief Market Research Officer of Quorum.

Your responsibility is to analyze the startup idea from a market perspective.

Startup Title:
{idea.title}

Description:
{idea.description}

Target Users:
{idea.target_users}

Previous Board Discussion:
{board_context}

If the board discussion is empty, perform an independent analysis.

If previous executives have already made observations, DO NOT repeat them.
Build on their findings, point out agreements or disagreements, and add new market insights.

Return ONLY valid JSON.

{{
    "finding":"...",
    "recommendation":"Proceed or Modify or Reject",
    "vote":"Approve",
    "pros":[
        "...",
        "..."
    ],
    "cons":[
        "...",
        "..."
    ]
}}

The "vote" field MUST be exactly one of:

Approve
Modify
Reject

Never return Abstain or any other value.

Do not return markdown.
Do not return explanations.
Return JSON only.

If you disagree with a previous executive,
clearly explain why.

If you agree,
state what additional evidence supports that decision.

Do not blindly agree.

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

Act as an independent executive.
"""

        response = self.llm.generate(prompt)

        if response.startswith("ERROR"):

            return AgentResponse(
                agent_name=self.name,
                finding="Research analysis could not be completed.",
                recommendation="Retry",
                confidence=0,
                concerns=["LLM service unavailable"],
                vote=Vote.MODIFY
                )

        import json

        data = json.loads(response)

        vote_text = data.get("vote", "Modify").upper()

        if vote_text not in Vote.__members__:
            vote_text = "MODIFY"

        return AgentResponse(
        agent_name=self.name,
        finding=data["finding"],
        recommendation=data["recommendation"],
        confidence=self.confidence_engine.calculate(response),
        concerns=data["cons"],
        vote=Vote[vote_text]
        )