import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://client.test.sagicor.com/#/login")
driver.maximize_window()
time.sleep(10)
title = driver.title
print(title)
URL = driver.current_url
print(URL)
