from day8_caesar_cipher_art import logo
print(logo)


def encode(text, move):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    text = text.lower()
    encoded_message = ""
    for ch in text:
        if ch in letters:
            index = letters.index(ch)
            index += move
            if index > 25:
                index = index - 26
            encoded_message += letters[index]
        else:
            encoded_message += ch
    print(f"Here's the encoded result: {encoded_message}")


def decode(text, move):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    text = text.lower()
    decoded_message = ""
    for ch in text:
        if ch in letters:
            index = letters.index(ch)
            index -= move
            if index < 0:
                index += 26
            decoded_message += letters[index]
        else:
            decoded_message += ch
    print(f"Here's the decoded result: {decoded_message}")


repeat = "yes"
while repeat == "yes":
    action = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if action == "encode":
        message = input("Type your message:\n")
        shift = int(input("Type the shift number:\n"))
        encode(message, shift)
    elif action == "decode":
        message = input("Type your message:\n")
        shift = int(input("Type the shift number:\n"))
        decode(message, shift)
    else:
        print("Invalid input")
    repeat = input("Type 'yes' if you want to go again. Otherwise type 'no' to exit:\n")
print("Exiting the cipher..")
