import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

class DemoAutosuggestion():
    def demo_Autosuggestion(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window( )
        time.sleep(2)
        depart_from = driver.find_element(By.XPATH, "//input[@class='required_field cityPadRight ac_input origin_ac']")
        depart_from.click()
        time.sleep(3)
        depart_from.send_keys("New Delhi")
        time.sleep(3)
        depart_from.send_keys(Keys.ENTER)
        time.sleep(3)
        going_to = driver.find_element(By.XPATH, "//input[@class='required_field cityPadLeft ac_input dest_ac']")
        going_to.send_keys("New")
        search_results = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        print(len(search_results))
        for result in search_results:
            print(result.text)
            if "New York (JFK)" in result.text:
                result.click()
                time.sleep(3)
                break

        origin_cal = driver.find_element(By.XPATH, "//input[@class='custom-date-input BE_flight_origin_date']")
        origin_cal.click()
        time.sleep(3)
        # driver.find_element(By.XPATH, "//td[@id = '28/08/2024']").click()
        # time.sleep(3)
        all_dates = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        for date in all_dates:
            if date.get_attribute("data-date") == '15/08/2024':
                date.click()
                time.sleep(4)
                break






Node1 = DemoAutosuggestion()
Node1.demo_Autosuggestion()