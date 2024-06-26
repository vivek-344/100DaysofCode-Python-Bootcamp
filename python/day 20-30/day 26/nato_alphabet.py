import pandas as pd

data = pd.read_csv("nato_phonetics.csv")

phonetics = {row.letter: row.code for (index, row) in data.iterrows()}

# loop_flag = True
#
# while loop_flag:
#     try:
#         word = input("Enter a word: ").upper()
#         phonetic_list = [phonetics[letter] for letter in word]
#     except KeyError:
#         print("Please enter only alphabets.")
#     else:
#         loop_flag = False
#         print(phonetic_list)


# Recursive Approach
def generate_phonetics():
    word = input("Enter a word: ").upper()
    try:
        phonetic_list = [phonetics[letter] for letter in word]
    except KeyError:
        print("Please enter only alphabets.")
        generate_phonetics()
    else:
        print(phonetic_list)


generate_phonetics()
