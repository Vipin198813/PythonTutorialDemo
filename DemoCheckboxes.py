import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Democheckboxes():
    def demo_checkboxes(self):
        driver = webdriver.Chrome()
        driver.get("https://seleniumbase.io/demo_page")
        driver.maximize_window( )
        time.sleep(20)
        DropdownItem = driver.find_element(By.ID, "mySelect")
        DD = Select(DropdownItem)
        DD.select_by_index(0)
        time.sleep(5)
        DD.select_by_visible_text("Set to 50%")
        time.sleep(5)
        DD.select_by_value("75%")
        time.sleep(5)




Node1 = Democheckboxes()
Node1.demo_checkboxes()