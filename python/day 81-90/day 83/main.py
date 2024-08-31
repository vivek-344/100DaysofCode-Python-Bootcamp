import os
import random


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


board = ['_'] * 9
chosen_a = []
chosen_b = []
choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
combinations = [
    [1, 2, 3],  # Top row
    [4, 5, 6],  # Middle row
    [7, 8, 9],  # Bottom row
    [1, 4, 7],  # Left column
    [2, 5, 8],  # Middle column
    [3, 6, 9],  # Right column
    [1, 5, 9],  # Diagonal from top-left to bottom-right
    [3, 5, 7]   # Diagonal from top-right to bottom-left
]


def display_board():
    clear_screen()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()


display_board()

while True:
    choice = 0
    while not choice:
        choice = int(input(f"Enter a choice from {choices}:\n"))
        if choice not in choices:
            print("Invalid Choice!")
            choice = 0
        else:
            choices.remove(choice)
            chosen_a.append(choice)
            board[choice - 1] = 'X'
            display_board()

    if any(all(pos in chosen_a for pos in combo) for combo in combinations):
        print("You Win!")
        break

    if not choices:
        print("It's a tie!")
        break

    choice = random.choice(choices)
    choices.remove(choice)
    chosen_b.append(choice)
    board[choice - 1] = 'O'
    display_board()

    if any(all(pos in chosen_b for pos in combo) for combo in combinations):
        print("You Lose!")
        break

    if not choices:
        print("It's a tie!")
        break
