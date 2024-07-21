import os
import time
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()

EMAIL = os.getenv("TWITTER_MAIL")
PASSWORD = os.getenv("TWITTER_PASSWORD")
PROMISED_DOWNLOAD = 10
PROMISED_UPLOAD = 2

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

x_url = "https://x.com/i/flow/login"
ookla_url = "https://www.speedtest.net/"
driver = webdriver.Edge(options=edge_options)
driver.get(ookla_url)

test_speed = driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
test_speed.click()

time.sleep(60)

d_speed = driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
download = float(d_speed.text)

up_speed = driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
upload = float(up_speed.text)

if download < PROMISED_DOWNLOAD or upload < PROMISED_UPLOAD:
    driver.get(x_url)

    time.sleep(5)

    username = driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div[2]/div/div[4]/label/div/div[2]/div/input')
    username.send_keys(EMAIL, Keys.ENTER)

    time.sleep(5)

    password = driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    password.send_keys(PASSWORD, Keys.ENTER)

    time.sleep(5)

    tweet_compose = driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

    tweet = f"Hey Internet Provider, why is my internet speed {download}down/{upload}up when I pay for {PROMISED_DOWNLOAD}down/{PROMISED_UPLOAD}up?"
    tweet_compose.send_keys(tweet)
    time.sleep(5)

    tweet_button = driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
    tweet_button.click()

    time.sleep(5)

driver.quit()
