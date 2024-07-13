from bs4 import BeautifulSoup
from datetime import datetime
import requests


def is_valid_date(date_str):
    try:
        # Try to parse the date string with the format YYYY-MM-DD
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False


date = ""
while True:
    date = input("Enter a date in YYYY-MM-DD format: ")
    if is_valid_date(date):
        break
    print("Invalid date!!")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")

soup = BeautifulSoup(response.text, "html.parser")

html_list = soup.find_all(class_="o-chart-results-list-row-container")

song_dict = {}

for item in html_list:
    song_dict[item.select_one("div ul li ul li span").text.strip()] = item.select_one("div ul li ul li h3").text.strip()

for key, value in song_dict.items():
    print(f"{key}: {value}")
