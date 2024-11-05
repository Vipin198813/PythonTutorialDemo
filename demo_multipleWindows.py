import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

class DemoMultipleWindows():
    def Demo_MultipleWindows(self):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/browser-windows")
        parent_handle = driver.current_window_handle
        print(parent_handle)
        driver.find_element(By.XPATH, "//button[@id='tabButton']").click()
        all_handles = driver.window_handles
        print(all_handles)
        for handles in all_handles:
            if handles != parent_handle:
                driver.switch_to.window(handles)
                text1 = driver.find_element(By.ID, "sampleHeading").text
                print(text1)
                time.sleep(3)
                driver.close()
                time.sleep(2)
                break
        driver.switch_to.window(parent_handle)
        
ddMultipleWindow = DemoMultipleWindows()
ddMultipleWindow.Demo_MultipleWindows()