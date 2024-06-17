names = open("names.txt", "r").readlines()

with open("letter.txt", "r") as letter:
    letter_text = letter.read()
    for name in names:
        message = letter_text.replace("[name]", name.strip())
        with open(f"./invitation_letters/letter_to_{name.strip()}", "w") as invitation_letter:
            invitation_letter.write(message)
