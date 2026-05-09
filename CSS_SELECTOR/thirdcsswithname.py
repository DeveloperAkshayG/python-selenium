"""
This script demonstrates css selector by name
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://artoftesting.com/samplesiteforselenium#")
driver.maximize_window()
time.sleep(5)

# text box locator
text=driver.find_element(By.CSS_SELECTOR,"input[name='firstName']")

# ENTER INPUT
text.send_keys("chintamani")
time.sleep(5)

# clear input
text.clear()
time.sleep(5)

# quit browser
driver.quit()