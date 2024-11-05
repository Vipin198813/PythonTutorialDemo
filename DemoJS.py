import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

class DemoJS():
    def demo_DemoJs(self):
        driver = webdriver.Chrome()
        # driver.get("https://training.rcvacademy.com/")
        driver.execute_script("window.open('https://training.rcvacademy.com/courses','_self');")
        time.sleep(4)
        demo_element = driver.execute_script("return document.getElementsByTagName('p')[1];")
        driver.execute_script("arguments[0].click();", demo_element)
        # driver.maximize_window( )


ddDemoJs = DemoJS()
ddDemoJs.demo_DemoJs()