from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

url = "http://secure-retreat-92358.herokuapp.com/"
driver = webdriver.Edge(options=edge_options)
driver.get(url)

f_name = driver.find_element(By.NAME, value="fName")
f_name.send_keys("Vivekraj")

l_name = driver.find_element(By.NAME, value="lName")
l_name.send_keys("Singh Sisodiya")

email = driver.find_element(By.NAME, value="email")
email.send_keys("random@gmail.com", Keys.ENTER)
