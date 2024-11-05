import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://client.test.sagicor.com/#/login")
driver.maximize_window()
print(driver.title)
driver.implicitly_wait(50)
driver.find_element(By.XPATH, "//button[@class='btn blue-btn']").is_displayed()
buttontext = driver.find_element(By.XPATH, "//button[@class='btn blue-btn']").text
print(buttontext)

time.sleep(10)