from tkinter import messagebox
from tkinter import *
import pyperclip
import string
import random


def generate_password():
    length = 12
    all_characters = string.ascii_letters + string.digits + string.punctuation

    generated_password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    generated_password += random.choices(all_characters, k=length - 4)

    random.shuffle(generated_password)
    password.delete(0, END)
    password.insert(0, ''.join(generated_password))
    pyperclip.copy(''.join(generated_password))


def add_entry():
    web = website.get()
    email = username.get()
    passcode = password.get()

    if len(web) == 0 or len(passcode) == 0 or len(email) == 0:
        messagebox.showinfo(title="Empty Fields", message="You cannot add empty fields.")
    else:
        confirmation = messagebox.askokcancel(title=web, message=f"Do you want to add the following entry?\nEmail = "
                                                                 f"{email}\nPassword = {passcode}")

        if confirmation:
            with open(file="passwords.txt", mode="a") as file:
                file.write(f"{web} | {email} | {passcode}\n")
                website.delete(0, END)
                password.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=48, pady=48)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1, pady=20)

label = Label(text="Website:")
label.grid(row=1, column=0, sticky="e")

label = Label(text="Email/Username:")
label.grid(row=2, column=0, sticky="e")

label = Label(text="Password:")
label.grid(row=3, column=0, sticky="e")

website = Entry(width=36)
website.grid(row=1, column=1, columnspan=2, pady=5)
website.focus()

username = Entry(width=36)
username.insert(END, string="vivekrajsingh344@gmail.com")
username.grid(row=2, column=1, columnspan=2, pady=5)

password = Entry(width=18)
password.grid(row=3, column=1, pady=5)

generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(row=3, column=2)

add_entry = Button(text="Add", command=add_entry, width=30)
add_entry.grid(row=4, column=1, columnspan=2, pady=10)

window.mainloop()
