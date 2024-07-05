import requests
import datetime as dt
from keys import TOKEN, USERNAME, GRAPH_ID

pixela_api_url = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

create_user = requests.post(url=pixela_api_url, json=user_params)

graph_params = {
    "id": GRAPH_ID,
    "name": "reading-habit",
    "unit": "Pages",
    "type": "int",
    "color": "ichou",
}

header = {
    "X-USER-TOKEN": TOKEN
}

create_graph = requests.post(url=f"{pixela_api_url}/{USERNAME}/graphs", json=graph_params, headers=header)

graph_url = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

pixel_params = {
    # "date": "".join(str(dt.datetime.today()).split()[0].split("-")),
    "date": dt.datetime.today().strftime("%Y%m%d"),
    "quantity": input("Enter the quantity to add: ")
}

post_pixel = requests.post(url=graph_url, headers=header, json=pixel_params)
print(post_pixel.text)
