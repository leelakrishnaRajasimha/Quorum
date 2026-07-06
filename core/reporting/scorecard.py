class ScoreCard:

    def generate(self, responses, decision):

        report = []

        report.append("=" * 80)
        report.append("QUORUM EXECUTIVE SCORECARD")
        report.append("=" * 80)
        report.append("")

        header = f"{'Executive':<18}{'Vote':<15}{'Confidence'}"
        report.append(header)
        report.append("-" * len(header))

        for response in responses:

            report.append(
                f"{response.agent_name:<18}"
                f"{response.vote.value:<15}"
                f"{str(response.confidence) + '%'}"
            )

        report.append("")
        report.append("-" * 80)
        report.append(f"Approved : {decision['approve']}")
        report.append(f"Modify   : {decision['modify']}")
        report.append(f"Rejected : {decision['reject']}")
        report.append(f"Average Confidence : {decision['confidence']}%")
        report.append(f"Final Decision : {decision['decision']}")
        report.append("=" * 80)

        return "\n".join(report)