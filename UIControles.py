import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("name") == 'checkBoxOption2':
        checkbox.click()
        assert checkbox.is_selected()
        break

radiobutton = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
print(len(radiobutton))
for button in radiobutton:
    if button.get_attribute("value") == "radio2":
        button.click()
        assert button.is_selected()
        break

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()

time.sleep(10)