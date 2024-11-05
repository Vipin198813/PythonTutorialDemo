import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service

driver : webdriver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
time.sleep(5)
windows_opened = driver.window_handles
driver.switch_to.window(windows_opened[1])
print(driver.find_element(By.TAG_NAME, "h3").text)