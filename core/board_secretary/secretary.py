import uuid
from datetime import datetime


class BoardSecretary:

    def __init__(self):
        self.meeting_minutes = []

        self.meeting_id = str(uuid.uuid4())[:8]

        self.created_at = datetime.now()

    def record(self, response):

        self.meeting_minutes.append({
            "agent": response.agent_name,
            "finding": response.finding,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "vote": response.vote.value
        })

    def generate_minutes(self):

        report = []

        report.append("=" * 80)
        report.append("QUORUM EXECUTIVE BOARD MEETING")
        report.append("=" * 80)
        report.append(f"Meeting ID : {self.meeting_id}")
        report.append(f"Generated : {self.created_at}")
        report.append("")

        for minute in self.meeting_minutes:

            report.append(f"Agent : {minute['agent']}")
            report.append(f"Confidence : {minute['confidence']}%")
            report.append(f"Vote : {minute['vote']}")
            report.append("")
            report.append(minute["finding"])
            report.append("")
            report.append("-" * 80)

        return "\n".join(report)