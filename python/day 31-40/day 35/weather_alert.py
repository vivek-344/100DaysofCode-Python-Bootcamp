from auth_keys import OPENWEATHER_API_KEY, TWILIO_SID, TWILIO_TOKEN
from twilio.rest import Client
import requests


# noinspection SpellCheckingInspection
params = {
    "lat": 23.3153043,
    "lon": 77.3625402,
    "cnt": 4,
    "appid": OPENWEATHER_API_KEY
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=params)
response.raise_for_status()
data = response.json()

id_list = []

for weather_data in data["list"]:
    for weather in weather_data["weather"]:
        id_list.append(weather["id"])

print(id_list)

for weather_id in id_list:
    if weather_id < 700:
        client = Client(TWILIO_SID, TWILIO_TOKEN)
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body="It's going to rain today. Remember to bring an umbrella. ☔",
            to="whatsapp:+918827962731",
        )
        break
