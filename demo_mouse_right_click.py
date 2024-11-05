import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

class DemoRightClick():
    def Demo_RightClick(self):
        driver = webdriver.Chrome( )
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()
        Achain = ActionChains(driver)
        Button1 = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
        Achain.context_click(Button1).perform()
        time.sleep(5)


dRightClick = DemoRightClick()
dRightClick.Demo_RightClick()