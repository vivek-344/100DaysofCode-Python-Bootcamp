import os
import requests
from dotenv import load_dotenv
from data_manager import DataManager

load_dotenv()

USERNAME = os.getenv("SHEETY_USERNAME")

sheety_url = f"https://api.sheety.co/{USERNAME}/flightDeals/prices"
sheety_response = requests.get(url=sheety_url)
airport_data = sheety_response.json()["prices"]
iata_codes = {airport["id"]: airport["iata"] for airport in airport_data}

for key in iata_codes.keys():
    DataManager.feed_data(key, "DEL", iata_codes[key], "2024-07-01", "INR")
