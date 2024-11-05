import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
#ID, Xpath, cssSelector,Class name, name, linkText
driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")


driver.find_element(By.ID,"exampleCheck1").click()

#//tagname[@attribute = 'value]
#input[@type = 'submit']
driver.find_element(By.XPATH,"//input[@type = 'submit']").click()
message =driver.find_element(By.CLASS_NAME,"alert-success").text
driver.find_element(By.CSS_SELECTOR, "input[name = 'name']").send_keys("Vipin")
print(message)
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

#Static Dropdown
dropdown1 = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown1.select_by_visible_text("Female")
time.sleep(10)
dropdown1.select_by_index(0)


assert  "Success" in message
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hello Again")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
time.sleep(10)