
from category import Category


class Quiz:
    category_names = [
        "animals", "brain-teasers", "celebrities", "entertainment",
        "for-kids", "general", "geography", "history", "hobbies",
        "humanities", "literature", "movies", "music", "newest",
        "people", "rated", "religion-faith", "science-technology",
        "sports", "television", "video-games", "world"
    ]

    def __init__(self):
        while True:
            print("Available categories:")
            for i in range(0, len(Quiz.category_names), 4):
                print(",  ".join(map(repr, Quiz.category_names[i: i+4])))
            chosen_category = input("Choose a category:\n> ")
            try:
                self.category = Category.new(chosen_category)
            except IOError:
                print("Category initialisation failed.")
                continue
            break
        self.number_wrong_answer = 0
        self.number_right_answer = 0

    @staticmethod
    def get_answer():
        while True:
            answer = input("enter your answer: ").upper()
            if answer not in ["A", "B", "C", "D"]:
                print("Invalid answer. Try again.")
            else:
                return answer

    def run_quiz(self):
        for question in self.category:
            print("\n", question, sep="")
            answer = Quiz.get_answer()
            if question.check_answer(answer) == True:
                print("well done")
                self.number_right_answer += 1
            else:
                print(
                    f"sorry, the correct answer was: {repr(question.correct)} try the next time")
                self.number_wrong_answer += 1

            if self.number_wrong_answer == 3:
                break
