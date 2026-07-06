from collections import Counter


class DecisionEngine:

    def calculate(self, responses):

        votes = Counter()

        total_confidence = 0

        for response in responses:

            votes[response.vote.value] += 1
            total_confidence += response.confidence

        average_confidence = round(
            total_confidence / len(responses),
            1
        )

        approve = votes.get("Approve", 0)
        modify = votes.get("Modify", 0)
        reject = votes.get("Reject", 0)

        if approve > modify and approve > reject:
            final = "APPROVED"

        elif modify > approve and modify > reject:
            final = "APPROVED WITH MODIFICATIONS"

        elif reject > approve and reject > modify:
            final = "REJECTED"

        else:
            final = "TIE - CEO DECIDES"

        return {
            "approve": approve,
            "modify": modify,
            "reject": reject,
            "confidence": average_confidence,
            "decision": final
        }