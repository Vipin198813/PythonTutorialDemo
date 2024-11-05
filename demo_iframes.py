import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


class DemoIFrames( ):
    def Demo_Iframes(self):
        driver = webdriver.Chrome( )
        driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe_target")
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='iframeResult']"))
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[@target='iframe_a']").click()
        time.sleep(4)


DemoIFrames = DemoIFrames( )
DemoIFrames.Demo_Iframes( )