from agents.research.research import ResearchAgent
from agents.finance.finance import FinanceAgent
from agents.product.product import ProductAgent
from agents.architecture.architecture import ArchitectureAgent
from agents.marketing.marketing import MarketingAgent
from agents.risk.risk import RiskAgent

from core.board_secretary.secretary import BoardSecretary
from core.communication.board_context import BoardContext
from core.orchestrator.decision_engine import DecisionEngine
from core.orchestrator.executive_summary import ExecutiveSummary
from core.reporting.scorecard import ScoreCard
from core.orchestrator.success_predictor import SuccessPredictor
from core.orchestrator.financial_projection import FinancialProjection
from core.orchestrator.investor_recommendation import InvestorRecommendation
from core.orchestrator.execution_plan import ExecutionPlan

class CEOAgent:

    def __init__(self, provider="gemini"):

        self.research = ResearchAgent(provider)
        self.finance = FinanceAgent(provider)
        self.product = ProductAgent(provider)
        self.architecture = ArchitectureAgent(provider)
        self.marketing = MarketingAgent(provider)
        self.risk = RiskAgent(provider)

        self.secretary = BoardSecretary()
        self.board_context = BoardContext()

        self.decision_engine = DecisionEngine()
        self.executive_summary = ExecutiveSummary()
        self.scorecard = ScoreCard()
        self.success_predictor = SuccessPredictor(provider)
        self.financial_projection = FinancialProjection(provider)
        self.investor = InvestorRecommendation(provider)
        self.execution_plan = ExecutionPlan(provider)

    def run_agent(self, agent, idea):

        response = agent.analyze(
            idea,
            self.board_context.get_summary()
        )

        self.board_context.add(response)
        self.secretary.record(response)

        return response

    def conduct_board_meeting(self, idea, progress_callback=None):

        print("\nBoard Meeting Started...\n")

        board_responses = []

        agents = [
            self.research,
            self.finance,
            self.product,
            self.architecture,
            self.marketing,
            self.risk
        ]

        for agent in agents:

            print(f"Running {agent.name} Agent...")

            response = self.run_agent(agent, idea)
            if progress_callback:
                progress_callback(agent.name)

            board_responses.append(response)

        print("\nBoard Meeting Completed.\n")

        minutes = self.secretary.generate_minutes()

        decision = self.decision_engine.calculate(board_responses)

        summary = self.executive_summary.generate(
            board_responses,
            decision
        )

        success = self.success_predictor.predict(idea, summary)
        financial = self.financial_projection.generate(idea, summary)
        investor = self.investor.generate(idea, summary)
        roadmap = self.execution_plan.generate(idea, summary)

        scorecard = self.scorecard.generate(
            board_responses,
            decision
        )

        return (
            minutes,
            decision,
            summary,
            scorecard,
            board_responses,
            success,
            financial,
            investor,
            roadmap
        )