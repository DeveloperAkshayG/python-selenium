import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# open browser
driver=webdriver.Chrome()
time.sleep(2)

# open url
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(2)

# select checkbox
checkbox_locator=driver.find_element(By.ID,"checkBoxOption1")
checkbox_locator.click()
time.sleep(2)
checkbox_locator.click()
time.sleep(2)
driver.close()
