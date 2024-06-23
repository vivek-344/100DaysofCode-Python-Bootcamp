from tkinter import *

window = Tk()
window.title("Miles to Kilometers")
window.minsize(width=540, height=360)
window.config(pady=72)

kilometers = "             "


def convert():
    try:
        global kilometers
        mile = float(miles_entry.get())
        kilometers = round(mile * 1.609344, 2)
        label.config(text=f"is equal to {kilometers} Km")
    except ValueError:
        label.config(text="Please enter a valid number")


label = Label(text="Miles to Kilometers Converter", font=("Ariel", 14, "bold"))
label.place(x=128, y=20)

miles_entry = Entry(width=10)
miles_entry.place(x=208, y=64)

label = Label(text="Miles")
label.place(x=278, y=63)

label = Label(text=f"is equal to {kilometers} Km")
label.place(x=188, y=88)

# result_label = Label(text="")
# result_label.place(x=254, y=88)
#
# label = Label(text="Km")
# label.place(x=294, y=88)

button = Button(text="Convert", command=convert)
button.place(x=224, y=118)

window.mainloop()
