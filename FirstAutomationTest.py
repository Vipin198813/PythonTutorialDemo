import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
driver.get("https://www.yatra.com/")
driver.maximize_window()
siteTitle = driver.title
print(siteTitle)
time.sleep(10)
driver.find_element(By.PARTIAL_LINK_TEXT, "Yatra").click()
time.sleep(5)
driver.close()