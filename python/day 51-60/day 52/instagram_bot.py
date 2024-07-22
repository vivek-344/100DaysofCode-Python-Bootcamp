import os
import time
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

ig_url = "https://www.instagram.com/"
driver = webdriver.Edge(options=edge_options)
driver.get(ig_url)

time.sleep(5)

username = driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
username.send_keys(EMAIL)

password = driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
password.send_keys(PASSWORD, Keys.ENTER)

time.sleep(10)

domestikcook_url = "https://www.instagram.com/domestikcook/"
driver.get(domestikcook_url)

time.sleep(5)

followers = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]'
                                                '/section/main/div/header/section[3]/ul/li[2]/div/a')
followers.click()

time.sleep(5)

followers_list = driver.find_elements(By.XPATH, value='/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]'
                                                      '/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div')

for follower in followers_list:
    button = follower.find_element(By.TAG_NAME, 'button')
    button.click()
    time.sleep(2)

driver.quit()
