"""
This script demonstrates how to apply implicit wait
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://proleed.academy/exercises/selenium/automation-practice-form-with-radio-button-check-boxes-and-drop-down.php")
driver.maximize_window()
driver.execute_script("window.scrollBy(0,800)")
time.sleep(2)

# implicit wait
driver.implicitly_wait(15)

# locator for martial status radio button divorced
element_martial_status=driver.find_element(By.ID,"divorced")

# select the radio button
element_martial_status.click()
time.sleep(5)

# quit browser
driver.quit()