import os
import random

from day14_higher_lower_game_art import logo
from day14_higher_lower_game_data import data


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


a = random.choice(data)
b = random.choice(data)
while a == b:
    b = random.choice(data)


def compare(x, y, z):
    if z == 'A' and x >= y:
        return True
    elif z == 'B' and y >= x:
        return True
    return False


count = 0
clear_screen()
print(logo)
while True:
    print(f"Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}")
    print(f"Against B: {b["name"]}, a {b["description"]}, from {b["country"]}")
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    clear_screen()
    print(logo)
    if guess == 'A' or guess == 'B':
        if compare(a["followers"], b["followers"], guess):
            count += 1
            print(f"Correct! Your score is {count}")
            a = b
            while a == b:
                b = random.choice(data)
        else:
            print(f"Game Over. Your final score is {count}\n")
            break
    else:
        print("Invalid Input!")
