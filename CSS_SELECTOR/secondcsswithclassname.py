"""
This script demonstrates css selector class name
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(5)

# locate with class name as css locator
ele_locator=driver.find_element(By.CSS_SELECTOR,"input.input_error")

# ENTER INPUT
ele_locator.send_keys("standard_user")
time.sleep(5)

# clear input
ele_locator.clear()
time.sleep(5)

# quit browser
driver.quit()