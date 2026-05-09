"""
This script demonstrates css selector by name
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# instantiate driver
driver=webdriver.Chrome()

# OPEN URL
driver.get("https://proleed.academy/exercises/selenium/automation-practice-form-with-radio-button-check-boxes-and-drop-down.php")
driver.maximize_window()
time.sleep(5)

# id element locator
ele_locator=driver.find_element(By.CSS_SELECTOR,"input[name='identity_number']")

# enter input
ele_locator.send_keys("AIEPG1201G")
time.sleep(5)

# clear input
ele_locator.clear()
time.sleep(5)

# quit brower
driver.quit()