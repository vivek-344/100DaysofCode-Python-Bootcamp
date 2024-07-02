import random


class QuizLogic:
    def __init__(self, que_list):
        self.question_number = 0
        self.question_list = que_list

    def question(self):
        que = random.choice(self.question_list)
        self.question_number += 1
        self.question_list.remove(que)
        return que