from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

count = 0
timer = ""
break_count = 0
mode = "work"


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global count, break_count, mode, timer
    window.after_cancel(timer)
    count = 0
    break_count = 0
    mode = "work"
    update_timer_display("00:00")
    label.config(text="Timer", fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global count, mode
    if mode == "work":
        set_mode(WORK_MIN, "Work", GREEN)
    elif mode == "short_break":
        set_mode(SHORT_BREAK_MIN, "Break", PINK)
    elif mode == "long_break":
        set_mode(LONG_BREAK_MIN, "Break", RED)
    countdown(count)


def set_mode(minutes, text, color):
    global count
    count = minutes * 60
    label.config(text=text, fg=color)
    update_timer_display(format_time(count))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(time):
    global timer
    update_timer_display(format_time(time))
    if time > 0:
        timer = window.after(1000, countdown, time - 1)
    else:
        switch_mode()


def switch_mode():
    global mode, break_count
    if mode == "work":
        break_count += 1
        if break_count == 4:
            mode = "long_break"
            break_count = 0
        else:
            mode = "short_break"
    else:
        mode = "work"

    if mode == "work":
        set_mode(WORK_MIN, "Work", GREEN)
    elif mode == "short_break":
        set_mode(SHORT_BREAK_MIN, "Break", PINK)
    elif mode == "long_break":
        set_mode(LONG_BREAK_MIN, "Break", RED)


def update_timer_display(time_text):
    canvas.itemconfig(timer_text, text=time_text)


def format_time(time):
    minutes = time // 60
    seconds = time % 60
    return f"{minutes:02d}:{seconds:02d}"


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=64, pady=64, bg=YELLOW)

canvas = Canvas(width=256, height=256, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="pomodoro.png")
canvas.create_image(128, 112, image=image)
timer_text = canvas.create_text(128, 128, text="25:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

label = Label(text="Timer", font=(FONT_NAME, 52, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
label.grid(row=0, column=1)

start_button = Button(text="Start", command=start)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset)
reset_button.grid(row=2, column=2)

label = Label(text="Work", font=(FONT_NAME, 16, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
label.grid(row=3, column=1)

window.mainloop()
