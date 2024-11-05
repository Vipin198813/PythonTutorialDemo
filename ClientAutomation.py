import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service

driver : webdriver = webdriver.Chrome()
driver.get("https://client.test.sagicor.com/#/login")
time.sleep(30)
driver.find_element(By.XPATH, "//button[@class = 'btn blue-btn']").click()