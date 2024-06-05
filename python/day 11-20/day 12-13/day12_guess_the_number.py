import random


def check_number(num, turns):
    if num == key:
        return True
    elif turns == 0:
        return False
    elif key > num:
        print("Too low.")
    else:
        print("Too high.")
    return False


def game(attempts):
    print(f"You have {attempts} attempts to guess the number.")
    while attempts != 0:
        number = int(input("Make a guess: "))
        attempts -= 1
        if check_number(number, attempts):
            break
        print(f"You have {attempts} attempts remaining to guess the number.")
    if attempts == 0:
        print(f"You Lose. The number was {key}")
    else:
        print(f"You Win. The number is {key}")


print("Welcome to the Guess The Number Game!")
print("I'm thinking of a number between 1 and 100")
key = random.randint(1, 100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == 'easy':
    game(10)
elif difficulty == 'hard':
    game(5)
else:
    print("Invalid Input.")
