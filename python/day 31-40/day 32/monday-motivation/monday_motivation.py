from mail_password import EMAIL, PASSWORD
import datetime as dt
import smtplib
import random

if dt.datetime.now().weekday() == 4:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        with open("quotes.txt") as quotes:
            all_quotes = quotes.readlines()
            quote = random.choice(all_quotes)
            connection.sendmail(EMAIL, "vivekrajsingh344@gmail.com", msg=f"Subject:Monday Motivation\n\n{quote}")
