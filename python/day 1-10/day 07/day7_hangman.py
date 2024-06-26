import random, os


from day7_hangman_words import words
from day7_hangman_art import logo
from day7_hangman_art import stages

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']

word_list = words.split()
random_word = random.choice(word_list)

answer = []

for letter in random_word:
    answer += "_"

lives = 6

print(logo)

while lives != 0 and '_' in answer:
    ch = input("Guess a letter: ").strip().lower()

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    if ch not in letters:
        print("Invalid input..")
    elif ch[0] in answer:
        print(f"You already guessed {ch[0]}")
    elif ch[0] in random_word:
        for i in range(0, len(answer)):
            if random_word[i] == ch:
                answer[i] = ch
    else:
        lives -= 1
        print("You lost a life.")
    for ch in answer:
        print(ch, end=" ")
    print()
    print(stages[lives])

if lives > 0:
    print("You Win!")
else:
    print(f"You lose. The word was {random_word}")
