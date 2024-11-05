import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Nodefind():
    def nodefind1(self):
        driver = webdriver.Chrome()
        driver.get("https://client.test.sagicor.com/#/login")
        time.sleep(20)
        driver.find_element(By.XPATH, "//span[@class='icon fa fa-instagram']").click()


Node1 = Nodefind()
Node1.nodefind1()