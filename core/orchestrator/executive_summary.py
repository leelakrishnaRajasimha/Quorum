class ExecutiveSummary:

    def generate(self, responses, decision):

        summary = []

        summary.append("=" * 80)
        summary.append("CEO EXECUTIVE SUMMARY")
        summary.append("=" * 80)
        summary.append("")

        summary.append(
            f"The Executive Board has completed its evaluation."
        )

        summary.append(
            f"Final Decision : {decision['decision']}"
        )

        summary.append(
            f"Average Confidence : {decision['confidence']}%"
        )

        summary.append("")

        summary.append("Executive Highlights:")

        for response in responses:

            finding = response.finding.replace("\n", " ")

            if len(finding) > 180:
                finding = finding[:180] + "..."

            summary.append(
                f"- {response.agent_name}: {finding}"
            )

        summary.append("")
        summary.append("CEO Recommendation:")

        if decision["decision"] == "APPROVED":

            summary.append(
                "The board recommends proceeding with execution."
            )

        elif decision["decision"] == "APPROVED WITH MODIFICATIONS":

            summary.append(
                "Proceed after addressing the concerns raised during the meeting."
            )

        else:

            summary.append(
                "The proposal should be revised before reconsideration."
            )

        return "\n".join(summary)