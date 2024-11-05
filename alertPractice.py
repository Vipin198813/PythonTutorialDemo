import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

name = "rahul"
driver: WebDriver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID, "name").send_keys("Rahul")
driver.find_element(By.ID,"alertbtn").click()
alert = driver.switch_to.alert
alerttext = alert.text
print(alerttext)
assert name in alerttext
time.sleep(10)
alert.accept()