from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

soup = BeautifulSoup(response.text, "html.parser")

scores = soup.find_all(class_="score")
max_points = 0
max_score = None

for score in scores:
    points = int(score.text.split(" ")[0])
    if points > max_points:
        max_score = score
    max_points = max(max_points, points)

max_score_id = max_score.get("id").split("_")[1]

article_html = soup.find(id=max_score_id)

article = article_html.select_one("tr td span a")
rank = article_html.find(class_="rank").text

print(f"{rank} {article.text}")
print(article.get("href"))
