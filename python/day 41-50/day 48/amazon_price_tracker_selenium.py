import os
import smtplib
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()

SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

url = "https://www.amazon.in/Crucial-16GB-Laptop-Memory-CT16G4SFRA32A/dp/B08C511GQH"
driver = webdriver.Edge(options=edge_options)
driver.get(url)

unformatted_price = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price = float(unformatted_price.text.replace(",", ""))

trigger_price = 3000.00

title = driver.find_element(By.ID, value="productTitle").text

driver.quit()

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
