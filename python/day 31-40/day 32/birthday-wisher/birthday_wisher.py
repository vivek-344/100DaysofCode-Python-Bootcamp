from mail_password import EMAIL, PASSWORD
import datetime as dt
import pandas as pd
import smtplib
import random

date = dt.datetime.now()
df = pd.read_csv("birthdays.csv")
df_dict = df.to_dict(orient="records")

for entry in df_dict:
    if date.month == entry["month"] and date.day == entry["day"]:
        with open(f"./letter-templates/letter_{random.randint(1, 12)}.txt") as letter:
            letter_text = letter.read()
            message = letter_text.replace("[NAME]", entry["name"].strip())
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            connection.sendmail(EMAIL, entry["email"],
                                msg=f"Subject:Happy Birthday!\n\n{message}")
