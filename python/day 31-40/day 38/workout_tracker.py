from keys import NUTRITIONIX_API_KEY, NUTRITIONIX_APP_ID, SHEETY_USERNAME, SHEETY_AUTH_KEY
import datetime as dt
import requests

nutritionix_headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY
}

nutritionix_params = {
    "query": input("What exercises have you done?: ")
}

date_time = dt.datetime.today()

nutritionix_workout_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=nutritionix_workout_url, headers=nutritionix_headers, json=nutritionix_params)

print(response.json())

for exercises in response.json()["exercises"]:
    date = date_time.strftime("%d/%m/%Y")
    time = date_time.strftime("%H:%M:%S")
    exercise = exercises["name"].title()
    duration = exercises["duration_min"]
    calories = exercises["nf_calories"]

    sheety_url = f"https://api.sheety.co/{SHEETY_USERNAME}/myWorkouts/workouts"

    sheety_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories
        }
    }

    sheety_headers = {
        "Authorization": SHEETY_AUTH_KEY
    }

    sheety = requests.post(url=sheety_url, json=sheety_params, headers=sheety_headers)
    print(sheety.json())
