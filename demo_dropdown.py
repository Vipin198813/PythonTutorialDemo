import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

class Demodropdown():
    def demo_dropdown(self):
        driver = webdriver.Chrome()
        driver.get("https://www.salesforce.com/au/form/signup/freetrial-sales/?d=topnav2-btn-ft")
        driver.maximize_window()
        dropdown = driver.find_element(By.NAME,"UserTitle")
        dd = Select(dropdown)
        dd.select_by_index(1)
        time.sleep(3)
        dd.select_by_value("Sales_Manager_ANZ")
        time.sleep(3)
        dd.select_by_visible_text("Sales Manager")
        time.sleep(5)


dddemo = Demodropdown()
dddemo.demo_dropdown()