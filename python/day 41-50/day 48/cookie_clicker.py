import time
from selenium import webdriver
from selenium.webdriver.common.by import By

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

url = "https://orteil.dashnet.org/experiments/cookie/"
driver = webdriver.Edge(options=edge_options)
driver.get(url)

cookie = driver.find_element(By.XPATH, value='//*[@id="cookie"]')

start = time.time()

while time.time() - start < 300:
    start_time = time.time()
    while time.time() - start_time < 5:
        cookie.click()
    buyButtons = [button for button in driver.find_elements(By.XPATH, value='//*[@id="store"]/div')
                  if not button.get_attribute('class')]
    if buyButtons:
        buyButtons[len(buyButtons) - 1].click()

print(driver.find_element(By.XPATH, value='//*[@id="cps"]').text)

driver.quit()
