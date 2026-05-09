"""
This script demonstrates css selector class name
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

# text box locator
text_box_locator=driver.find_element(By.CSS_SELECTOR,"input.form-control")

# enter input
text_box_locator.send_keys("Rohit")
time.sleep(5)

# clear input
text_box_locator.clear()
time.sleep(5)

# quit browser
driver.quit()
