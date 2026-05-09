"""
This script demonstrates css selector with id
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# instantiate driver
driver=webdriver.Chrome()

# OPEN URL
driver.get("https://rahulshettyacademy.com/AutomationPractice/#")
driver.maximize_window()
time.sleep(5)

# css selector by id
username=driver.find_element(By.CSS_SELECTOR,"#name")

# input username
username.send_keys("joe root")
time.sleep(5)

# clear input
username.clear()
time.sleep(5)

# quit browser
driver.quit()