from dataclasses import dataclass, field
from enum import Enum
from typing import List


class Vote(Enum):
    APPROVE = "Approve"
    REJECT = "Reject"
    MODIFY = "Modify"


@dataclass
class AgentResponse:
    agent_name: str
    finding: str
    recommendation: str
    confidence: int
    concerns: List[str] = field(default_factory=list)
    vote: Vote = Vote.APPROVE


@dataclass
class StartupIdea:
    title: str
    description: str
    budget: str
    timeline: str
    target_users: str


@dataclass
class ExecutiveDecision:
    overall_score: int
    final_vote: Vote
    summary: str