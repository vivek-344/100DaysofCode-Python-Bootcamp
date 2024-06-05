# random module is imported to get some random value
# randrange(start, stop, step)
# randint(a, b)
# Read more.. https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if input != 0 or input != 1 or input != 2:
    print("Invalid input. You lose")
else:
    print(options[choice])

    print("Computer chose:")
    computer = random.randint(0, 2)
    print(options[computer])

    if computer == choice:
        print("It's a draw")
    elif choice == 0 and computer == 1:
        print("You lose")
    elif choice == 0 and computer == 2:
        print("You win")
    elif choice == 1 and computer == 0:
        print("You win")
    elif choice == 1 and computer == 2:
        print("You lose")
    elif choice == 2 and computer == 0:
        print("You lose")
    elif choice == 2 and computer == 1:
        print("You win")
