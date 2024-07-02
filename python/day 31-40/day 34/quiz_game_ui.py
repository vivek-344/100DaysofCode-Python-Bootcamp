import html
from tkinter import *
from tkinter import messagebox, simpledialog


THEME_COLOR = "#2C424E"


class QuizUI:
    def __init__(self, quiz_logic, user_input):
        self.question = None
        self.user_input = user_input
        self.quiz = quiz_logic
        self.point = 0

        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text="Score: 0")
        self.score.config(fg="white", bg=THEME_COLOR, highlightthickness=0, font=("Ariel", 12, "normal"))
        self.score.grid(row=0, column=1, padx=30, pady=(20, 10), sticky="e")

        self.canvas = Canvas(width=300, height=250)
        self.canvas_text = self.canvas.create_text(150, 125, text="question", width=275,
                                                   fill=THEME_COLOR, font=("Ariel", 16, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, rowspan=2, padx=20, pady=20)

        true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_image, command=self.correct)
        self.true_button.config(bg=THEME_COLOR, highlightthickness=0)
        self.true_button.grid(row=3, column=0, padx=20, pady=(20, 10))

        false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_image, command=self.incorrect)
        self.false_button.config(bg=THEME_COLOR, highlightthickness=0)
        self.false_button.grid(row=3, column=1, padx=20, pady=(20, 10))

        self.get_question()

        self.window.mainloop()

    @staticmethod
    def get_number_of_questions():
        return simpledialog.askinteger("Input", "How many questions would you like? (1-100)",
                                       minvalue=1, maxvalue=100)

    def get_question(self):
        if self.user_input > 0:
            self.question = self.quiz.question()
            q_text = html.unescape(self.question.text)
            self.canvas.itemconfig(self.canvas_text, text=f"Q.{self.quiz.question_number}: {q_text}")
            self.canvas.config(bg="white")
            self.enable_buttons()
        else:
            messagebox.showinfo("Quiz Completed!", f"Your final score is: {self.point}/{self.quiz.question_number}.")
            self.window.destroy()

    def update_score(self, is_correct):
        self.disable_buttons()
        if is_correct and self.user_input > 0:
            self.canvas.config(bg="green")
            self.point += 1
            self.score.config(text=f"Score: {self.point}")
        elif self.user_input > 0:
            self.canvas.config(bg="red")
        self.user_input -= 1
        self.window.after(1000, self.get_question)

    def correct(self):
        self.update_score(self.question.answer == "True")

    def incorrect(self):
        self.update_score(self.question.answer == "False")

    def disable_buttons(self):
        self.true_button.config(state=DISABLED)
        self.false_button.config(state=DISABLED)

    def enable_buttons(self):
        self.true_button.config(state=NORMAL)
        self.false_button.config(state=NORMAL)
