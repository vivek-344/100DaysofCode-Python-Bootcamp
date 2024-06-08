import random


class QuizLogic:
    def __init__(self, que_list):
        self.question_number = 0
        self.question_list = que_list
        self.points = 0

    def run(self, no_of_que):
        return self.question_number < no_of_que

    def check(self, guess, que):
        if que.answer.lower() == guess:
            self.points += 1
            print(f"Correct! The answer is: {que.answer}")
        else:
            print(f"That's wrong! The answer was: {que.answer}")
        print(f"Your current score is: {self.points}/{self.question_number}\n")

    def question(self):
        que = random.choice(self.question_list)
        self.question_number += 1
        guess = input(f"Q.{self.question_number}: {que.text} (True/False)?: ").lower()
        while guess not in ["true", "false"]:
            print("\nInvalid Input!!")
            guess = input(f"Q.{self.question_number}: {que.text} (True/False)?: ").lower()
        self.check(guess, que)
        self.question_list.remove(que)
