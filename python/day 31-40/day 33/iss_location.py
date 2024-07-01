from mail_password import EMAIL, PASSWORD
import requests
import datetime
import smtplib
import time


LATITUDE = 23.3153043
LONGITUDE = 77.3625402


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    position = response.json()["iss_position"]

    latitude = float(position["latitude"])
    longitude = float(position["longitude"])

    if abs(latitude - LATITUDE) < 5 and abs(longitude - LONGITUDE) < 5:
        return True
    return False


def is_night():
    my_location = {
        "lat": LATITUDE,
        "lng": LONGITUDE,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=my_location)
    response.raise_for_status()
    suntime = response.json()["results"]

    sunrise = int(suntime["sunrise"].split("T")[1].split(":")[0])
    sunset = int(suntime["sunset"].split("T")[1].split(":")[0])

    currTime = datetime.datetime.now()
    hour = (currTime - datetime.timedelta(hours=5, minutes=30)).hour

    if sunrise > hour or sunset < hour:
        return True
    return False


while True:
    time.sleep(60)
    print("Fetching data...")
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            connection.sendmail(EMAIL, "vivekrajsingh344@gmail.com",
                                msg=f"Subject:ISS Above!\n\nLook Up!")
