import os
import smtplib

from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests

load_dotenv()

SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8,en-IN;q=0.7"
}

url = "https://www.amazon.in/dp/B08C511GQH"

response = requests.get(url=url, headers=header)

soup = BeautifulSoup(response.text, "html.parser")

unformatted_price = soup.find(class_="a-price-whole").text.replace(',', '')
price = float(unformatted_price.split(".")[0])

trigger_price = 3000.00

title = soup.find(id="productTitle").get_text().strip()

if price < trigger_price:
    message = f"{title} is on sale for {price}!"

    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_ADDRESS,
            to_addrs=EMAIL_ADDRESS,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )
