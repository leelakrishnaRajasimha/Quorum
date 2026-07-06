from core.models.models import StartupIdea
from agents.ceo.ceo import CEOAgent

idea = StartupIdea(
    title="AI Fitness App",
    description="An AI app that creates personalized workouts and diet plans.",
    budget="₹10 Lakhs",
    timeline="6 Months",
    target_users="College Students"
)

ceo = CEOAgent()

meeting, decision, summary, scorecard, board_responses = ceo.conduct_board_meeting(idea)

print(meeting)

print("\n")
print("=" * 70)
print("EXECUTIVE BOARD DECISION")
print("=" * 70)

print(f"Approved : {decision['approve']}")
print(f"Modify   : {decision['modify']}")
print(f"Rejected : {decision['reject']}")
print(f"Confidence : {decision['confidence']}%")
print(f"Final Decision : {decision['decision']}")

print()
print(scorecard)

print()
print(summary)