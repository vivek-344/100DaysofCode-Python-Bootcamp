from morse_code import code

text = input("Enter String: ").lower().strip()

for ch in text:
    print(code[ch], end=" ")
