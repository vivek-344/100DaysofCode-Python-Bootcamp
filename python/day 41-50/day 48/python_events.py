from selenium import webdriver
from selenium.webdriver.common.by import By

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

url = "https://www.python.org/"
driver = webdriver.Edge(options=edge_options)
driver.get(url)

events_raw = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')

events_list = []

for event in events_raw:
    text = event.text
    events_list.append({"date": text.split("\n")[0], "event": text.split("\n")[1]})

events = {key: events_list[key] for key in range(0, len(events_list) - 1)}

print(events)

driver.quit()
