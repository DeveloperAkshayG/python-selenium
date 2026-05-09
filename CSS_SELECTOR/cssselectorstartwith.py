"""
This script demonstrates css selector locator startswith
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://proleed.academy/exercises/selenium/automation-practice-form-with-radio-button-check-boxes-and-drop-down.php")
driver.maximize_window()
time.sleep(5)

# element locator for first name start with fir
ele_locator=driver.find_element(By.CSS_SELECTOR,"input[name^='fir']")

# enter input
ele_locator.send_keys("chintamani")
time.sleep(5)

# clear input
ele_locator.clear()
time.sleep(5)

# quit browser
driver.quit()