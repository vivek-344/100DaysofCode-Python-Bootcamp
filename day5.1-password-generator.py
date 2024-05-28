import random

password_list = []
password = ""
rand = 0

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

no_letters = int(input("How many letters would you like in your password?\n"))
no_symbols = int(input("How many symbols would you like?\n"))
no_numbers = int(input("How many numbers would you like?\n"))

for i in range(0, no_letters):
    password_list += random.choice(letters)
for j in range(0, no_symbols):
    password_list += random.choice(symbols)
for k in range(0, no_numbers):
    password_list += random.choice(numbers)

random.shuffle(password_list)

for ch in password_list:
    password += ch

print(password)
