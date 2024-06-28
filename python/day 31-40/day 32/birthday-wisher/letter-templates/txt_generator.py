msg = ["Happy birthday! May your day be filled with joy and laughter!",
       "Happy Birthday! Enjoy your special day to the fullest!",
       "Happy birthday! Here's to another year of adventures and happiness!",
       "Wishing you a very happy birthday and a year filled with blessings!",
       "Happy Birthday! Make every moment unforgettable!",
       "Happy birthday! May your day be as amazing as you are!",
       "Wishing you a day filled with love, laughter, and cake! Happy birthday!",
       "Happy Birthday! Celebrate like there's no tomorrow!",
       "Happy birthday! May this year be your best one yet!"]

for i in range(4, 13):
    with open(f"letter_{i}.txt", mode="w") as file:
        file.write(f"Dear [NAME],\n\n{msg[i-4]}\n\nVivek")
