class StartupScore:

    def calculate(self, responses):

        total = 0

        for response in responses:
            total += response.confidence

        score = round(total / len(responses), 1)

        if score >= 90:
            grade = "A+"

        elif score >= 80:
            grade = "A"

        elif score >= 70:
            grade = "B"

        elif score >= 60:
            grade = "C"

        else:
            grade = "D"

        return {
            "score": score,
            "grade": grade
        }