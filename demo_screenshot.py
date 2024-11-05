import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

class DemoScreenshot():
    def demo_Screenshot(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window( )
        continue_demo = driver.find_element(By.XPATH, "//button[@id='login-continue-btn']")
        continue_demo.screenshot(".\\test.png")
        continue_demo.click()
        time.sleep(3)
        driver.get_screenshot_as_file("C:\\Users\\User\\PycharmProjects\\error.png")
        driver.save_screenshot(".\\test1.png")


Demoscreenshot1 = DemoScreenshot()
Demoscreenshot1.demo_Screenshot()