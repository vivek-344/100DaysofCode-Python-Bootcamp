import os
import requests
from amadeus import Client, ResponseError
from dotenv import load_dotenv

load_dotenv()


AMADEUS_KEY = os.getenv("AMADEUS_KEY")
AMADEUS_SECRET = os.getenv("AMADEUS_SECRET")
USERNAME = os.getenv("SHEETY_USERNAME")
sheety_url = f"https://api.sheety.co/{USERNAME}/flightDeals/prices"


class DataManager:
    @staticmethod
    def feed_data(row_id, origin, destination, date, currency):
        amadeus = Client(
            client_id=AMADEUS_KEY,
            client_secret=AMADEUS_SECRET
        )

        try:
            response = amadeus.analytics.itinerary_price_metrics.get(
                originIataCode=origin,
                destinationIataCode=destination,
                departureDate=date,
                currencyCode=currency
            )
        except ResponseError as error:
            print(f"An error occurred: {error}")
        else:
            sheety_row_url = f"{sheety_url}/{row_id}"
            sheety_params = {
                "price": {
                    "lowestPrice": response.data[0]["priceMetrics"][0]["amount"]
                }
            }
            requests.put(url=sheety_row_url, json=sheety_params)
            row_data = requests.get(sheety_row_url).json()
            print(row_data)
