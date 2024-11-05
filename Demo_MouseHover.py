import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class DemoMouseHover( ):
    def Demo_Mousehover(self):
        driver = webdriver.Chrome( )
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        morebutton = driver.find_element(By.XPATH, "//span[@class='more-arr']")
        achain = ActionChains(driver)
        achain.move_to_element(morebutton).perform()
        time.sleep(4)
        driver.find_element(By.XPATH,"//span[contains(text(), 'Xplore')]").click()
        time.sleep(4)

ddMouseHover = DemoMouseHover()
ddMouseHover.Demo_Mousehover()