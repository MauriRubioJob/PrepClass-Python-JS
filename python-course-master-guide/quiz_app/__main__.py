import config

from quiz import Quiz

while True:
    quiz = Quiz()
    quiz.run_quiz()

    print(f"You got {quiz.number_right_answer} questions correct.")
