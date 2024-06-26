from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"


df = pd.read_csv("words/japanese_words.csv")
df_dict = df.to_dict(orient="records")
random.shuffle(df_dict)


def format_text(text):
    text = text.replace('; ', '\n')
    text = text.replace(', ', '\n')
    return text


def flip():
    global df_dict
    flashcard.itemconfig(flashcard_image, image=back_image)
    flashcard.coords(furigana_text, 400, 400)
    flashcard.itemconfig(original_text, text=format_text(df_dict[0]["English"]), fill="white",
                         font=("Ariel", 42, "normal"), justify="center")
    flashcard.itemconfig(furigana_text, text=df_dict[0]["Romaji"], fill="white")


def update(delete=False):
    global df_dict, timer

    window.after_cancel(timer)

    if delete:
        del df_dict[0]

    random.shuffle(df_dict)
    flashcard.coords(furigana_text, 400, 325)
    flashcard.itemconfig(flashcard_image, image=front_image)
    flashcard.itemconfig(original_text, text=df_dict[0]["Original"], fill="black", font=("Ariel", 80, "bold"))
    flashcard.itemconfig(furigana_text, text=df_dict[0]["Furigana"], fill="black", font=("Ariel", 42, "normal"))
    timer = window.after(5000, flip)


window = Tk()
window.title("Japanese Flashcards")
window.config(padx=48, pady=48, bg=BACKGROUND_COLOR, highlightthickness=0)

flashcard = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
flashcard_image = flashcard.create_image(400, 263, image=front_image)
original_text = flashcard.create_text(400, 200, text="", fill="black", font=("Ariel", 80, "bold"))
furigana_text = flashcard.create_text(400, 325, text="", fill="black", font=("Ariel", 42, "normal"))
flashcard.grid(row=0, column=0, columnspan=2)

timer = window.after(5000, flip)
update()

known_image = PhotoImage(file="./images/right.png")
known_button = Button(image=known_image, command=lambda: update(True))
known_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)
known_button.grid(row=1, column=0, pady=(24, 0))

unknown_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=unknown_image, command=update)
unknown_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)
unknown_button.grid(row=1, column=1, pady=(24, 0))


window.mainloop()
