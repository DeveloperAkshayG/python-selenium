"""
This script demonstrates css selector locator endswith
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# instantiate driver
driver=webdriver.Chrome()

# OPEN URL
driver.get("https://demo.guru99.com/test/login.html#")
driver.maximize_window()
time.sleep(5)

# password locator field that ends with d
pass_locator=driver.find_element(By.CSS_SELECTOR,"input[id$='d']")

# enter input
pass_locator.send_keys("admin@123")
time.sleep(5)

# clear input
pass_locator.clear()
time.sleep(5)

# quit browser
driver.quit()
