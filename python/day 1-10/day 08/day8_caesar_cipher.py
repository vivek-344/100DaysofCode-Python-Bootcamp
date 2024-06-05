from day8_caesar_cipher_art import logo
print(logo)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encode(text, move, direction):
    final_message = ""
    if direction == "decode":
        move *= -1
    for ch in text:
        if ch in letters:
            index = (letters.index(ch) + move) % 26
            final_message += letters[index]
        else:
            final_message += ch
    print(f"Here's the {direction}d result: {final_message}")


repeat = "yes"
while repeat == "yes":
    action = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if action in ("encode", "decode"):
        message = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n")) % 26
        encode(message, shift, action)
    else:
        print("Invalid input")
    repeat = input("Type 'yes' if you want to go again. Otherwise type 'no' to exit:\n")
print("Exiting the cipher..")
