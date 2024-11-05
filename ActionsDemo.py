import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service

driver : webdriver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
driver.implicitly_wait(5)
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.click(driver.find_element(By.XPATH, "//input[@id = 'checkBoxOption1']")).click().perform()

