from core.llm.llm_service import LLMService


class ExecutionPlan:

    def __init__(self, provider="gemini"):

        self.llm = LLMService(provider)

    def generate(self, idea, board_summary):

        prompt = f"""
You are an experienced startup mentor.

Startup

Title:
{idea.title}

Description:
{idea.description}

Executive Board Summary:

{board_summary}

Create a practical 90-day execution roadmap.

Return ONLY:

Week 1-2

Week 3-4

Month 2

Month 3

For every stage give 3-5 practical action items.

Be realistic.

Prioritize validation before scaling.
"""

        return self.llm.generate(prompt)