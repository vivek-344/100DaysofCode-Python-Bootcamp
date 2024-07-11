from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")

for i in range(99, -1, -1):
    element = soup.find(lambda tag: tag.get('data-test') == f"listicle-item-{i}")
    with open("movies.txt", "a") as file:
        file.write(f"{element.select_one("div h3").text}\n")
