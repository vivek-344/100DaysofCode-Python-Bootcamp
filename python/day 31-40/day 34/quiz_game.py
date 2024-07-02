from quiz_game_ui import QuizUI
from quiz_game_logic import QuizLogic
from quiz_game_data import fetch_questions
from quiz_game_question_model import Question


user_input = QuizUI.get_number_of_questions()
questions = fetch_questions(user_input)
question_bank = [Question(q["question"], q["correct_answer"]) for q in questions]
quiz_logic = QuizLogic(question_bank)
QuizUI(quiz_logic, user_input)
