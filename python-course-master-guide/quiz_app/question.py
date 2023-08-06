
class Question:
    def __init__(self, question_string):
        self.text, answers = question_string.split("\n^ ")
        self.correct, *self.possible_answers = answers.splitlines()

    def __repr__(self):
        return self.text + "\n" + "\n".join(self.possible_answers)

    def check_answer(self, answer_chose):
        answer_index = "ABCD".index(answer_chose)
        answer = self.possible_answers[answer_index]
        if answer.endswith(self.correct):
            return True
        else:
            return False
