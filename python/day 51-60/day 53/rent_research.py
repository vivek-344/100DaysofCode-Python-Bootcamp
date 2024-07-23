import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
response = requests.get("https://appbrewery.github.io/Zillow-Clone/")

soup = BeautifulSoup(response.text, "html.parser")

listings = soup.find_all(class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

data = []

for listing in listings:
    address = listing.select_one("li div div article div div a").text
    address = address.replace("\n", "").strip()
    link = listing.select_one("li div div article div div a").get("href")
    rent_raw = listing.select_one("li div div article div div div div span").text
    rent = rent_raw.split(" ")[0].replace("/mo", "").split('+')[0]
    listing_map = {
      "address": address,
      "rent": rent,
      "link": link
    }
    data.append(listing_map)


edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

form_url = "https://forms.gle/Sw5qsWkdWMS7k93n6"
driver = webdriver.Edge(options=edge_options)
driver.get(form_url)

for entry in data:
    time.sleep(1)

    address = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]'
                                                  '/div/div[1]/div/div[1]/input')
    address.send_keys(entry["address"])

    rent = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]'
                                               '/div/div[1]/div/div[1]/input')
    rent.send_keys(entry["rent"])

    link = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]'
                                               '/div/div[1]/div/div[1]/input')
    link.send_keys(entry["link"])

    submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit_button.click()

    new_response = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    new_response.click()

driver.quit()
