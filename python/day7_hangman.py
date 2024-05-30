import random

from day7_hangman_words import words
from day7_hangman_art import logo
from day7_hangman_art import stages

word_list = words.split()
random_word = random.choice(word_list)

answer = []

for letter in random_word:
    answer += "_"

lives = 6

print(logo)

while lives != 0 and '_' in answer:
    ch = input("Guess a letter: ").strip().lower()
    print("\n")
    if ch[0] in answer:
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
    print("You lose.")
