from day17_quiz_game_data import question_data
from day17_quiz_game_question_model import Question
from day17_quiz_game_logic import QuizLogic

question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

quiz = QuizLogic(question_bank)

no_of_que = 0
while no_of_que not in range(1, 101):
    no_of_que = int(input("How many questions would you like? (1-100): "))
    if no_of_que < 1 or no_of_que > 100:
        print("Invalid Input!!")
while quiz.run(no_of_que):
    quiz.question()

print("Congratulations!! You've completed the quiz!!")
print(f"Your final score is: {quiz.points}/{quiz.question_number}.")
