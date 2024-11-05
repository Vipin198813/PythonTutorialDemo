import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service

browserShortedVeggies = []
driver : webdriver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element((By.XPATH, "//span[text() = 'Veg/fruit name']")).click()
VegElement = driver.find_elements(By.XPATH, "//tr/td[1]")

# for ele in VegElement:
#     browserShortedVeggies.append(ele.text)
#
# # print(browserShortedVeggies)
# # #
# # originalList = browserShortedVeggies.copy()
# # originalList.sort()
# #
# # assert browserShortedVeggies == originalList