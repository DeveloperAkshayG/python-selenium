"""
This script demonstrates css selector locator startswith
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://demo.guru99.com/test/login.html#")
driver.maximize_window()
time.sleep(5)

# element locator for element starting with pass
ele_locator=driver.find_element(By.CSS_SELECTOR,"input[name^='pass']")

# entering input
ele_locator.send_keys("admin@123")
time.sleep(5)

# clear input
ele_locator.clear()
time.sleep(5)

# quit browser
driver.quit()