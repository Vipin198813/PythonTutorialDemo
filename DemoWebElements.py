import time
from selenium import webdriver
from selenium.webdriver.common.by import By
class DemoFindElementID():
    def locate_by_id_element(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.NAME, "login-input").send_keys("test@test.com")
        time.sleep(5)

findbyID = DemoFindElementID()
findbyID.locate_by_id_element()

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open a webpage
driver.get('http://example.com')

# Locate a web element by its ID
header = driver.find_element_by_id('header')

# Perform actions on the web element
print(header.text)  # Print the text of the header
header.click()      # Click the header

# Close the browser
driver.quit()
