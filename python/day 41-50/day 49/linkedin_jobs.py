import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()

EMAIL = os.getenv("LINKEDIN_EMAIL")
PASSWORD = os.getenv("LINKEDIN_PASSWORD")

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

url = "https://www.linkedin.com/"
driver = webdriver.Edge(options=edge_options)
driver.get(url)

sign_in = driver.find_element(By.XPATH, value='/html/body/nav/div/a[2]')
sign_in.click()

username = driver.find_element(By.XPATH, value='//*[@id="username"]')
username.send_keys(EMAIL)

password = driver.find_element(By.XPATH, value='//*[@id="password"]')
password.send_keys(PASSWORD, Keys.ENTER)

time.sleep(30)

jobs_tab = driver.find_element(By.XPATH, value='//*[@id="global-nav"]/div/nav/ul/li[3]/a')
jobs_tab.click()

time.sleep(5)

search = driver.find_element(By.XPATH, value='/html/body/div[5]/header/div/div/div/div[2]/div[2]/div/div/input[1]')
search.send_keys("Python Developer", Keys.ENTER)

time.sleep(20)

postings = driver.find_elements(by=By.XPATH,
                                value='/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul/li')

for posting in postings:
    posting.click()
    save_job = driver.find_element(By.XPATH,
                                   value='/html/body/div[4]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]'
                                         '/div/div[1]/div/div[1]/div/div[1]/div[1]/div[6]/div/button')
    save_job.click()

    follow_org = driver.find_element(By.XPATH, value='/html/body/div[4]/div[3]/div[4]/div/div/main/div/div[2]/div[2]'
                                                     '/div/div[2]/div/div[1]/div/section/section/div[1]/div[1]/button')
    follow_org.click()

    time.sleep(5)

driver.quit()
