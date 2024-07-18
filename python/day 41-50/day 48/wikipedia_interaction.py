from selenium import webdriver
from selenium.webdriver.common.by import By

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

url = "https://en.wikipedia.org/wiki/Main_Page"
driver = webdriver.Edge(options=edge_options)
driver.get(url)

total_articles = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')

print(total_articles.text)

driver.quit()
