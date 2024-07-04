import requests
from twilio.rest import Client
from auth_keys import NEWSAPI_KEY, STOCK_API_KEY, TWILIO_SID, TWILIO_TOKEN

message = ""

stock_api_url = "https://latest-stock-price.p.rapidapi.com/equities"
news_api_url = "https://newsdata.io/api/1/latest"

stock_api_headers = {
    "x-rapidapi-key": STOCK_API_KEY,
    "x-rapidapi-host": "latest-stock-price.p.rapidapi.com"
}

stock_api_params = {
    "ISIN": "INE669E01016"
}

stock_api_response = requests.get(stock_api_url, headers=stock_api_headers, params=stock_api_params)

for stock in stock_api_response.json():
    name = stock["Name"]
    sym = stock["Symbol"]
    p_close = float(stock["P Close"])
    change = float(stock["Net Change"])
    percentage = round((change*100)/p_close, 2)
    if percentage >= 0:
        message += f"{name}: 🔺{abs(percentage)}\n\n"
    else:
        message += f"{name}: 🔻{abs(percentage)}\n\n"

    params = {
        "q": f"{name} OR {sym}",
        "language": "en",
        "country": "in",
        "apikey": NEWSAPI_KEY
    }

    news = requests.get(url=news_api_url, params=params)
    news.raise_for_status()
    if news.json()["results"]:
        message += f"Title: {news.json()["results"][0]["title"]}\n"
        message += f"Description: {news.json()["results"][0]["description"]}\n"
        message += f"Source: {news.json()["results"][0]["link"]}\n\n"

print(message)

client = Client(TWILIO_SID, TWILIO_TOKEN)
client.messages.create(
    from_="whatsapp:+14155238886",
    body=message,
    to="whatsapp:+918827962731",
)
