class BoardContext:

    def __init__(self):
        self.context = []

    def add(self, response):

        self.context.append({
            "agent": response.agent_name,
            "finding": response.finding,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "vote": response.vote.value
        })

    def get_summary(self):

        if not self.context:
            return "No previous discussion."

        summary = ""

        for item in self.context:

            summary += f"""
Agent : {item['agent']}
Vote : {item['vote']}
Confidence : {item['confidence']}
Recommendation : {item['recommendation']}

Finding:
{item['finding']}

----------------------------------
"""

        return summary