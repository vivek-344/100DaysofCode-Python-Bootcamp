import pandas as pd

data = pd.read_csv("nato_phonetics.csv")

phonetics = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()

phonetic_list = [phonetics.get(letter) for letter in word]

print(phonetic_list)
