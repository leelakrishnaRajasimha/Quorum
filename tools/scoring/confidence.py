class ConfidenceEngine:

    def calculate(self, text: str) -> int:

        score = 50

        words = len(text.split())

        if words > 80:
            score += 10

        if words > 150:
            score += 10

        if "recommend" in text.lower():
            score += 10

        if "risk" in text.lower():
            score += 5

        if "opportunity" in text.lower():
            score += 5

        return min(score, 100)