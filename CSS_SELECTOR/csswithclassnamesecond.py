"""
This script demonstrates css selector class name
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

# radio button locator
radio_button_locator=driver.find_element(By.CSS_SELECTOR,"input.Performance")

# click checkbox performance button
radio_button_locator.click()
time.sleep(5)

# unclick performance checkbox button
radio_button_locator.click()
time.sleep(5)

# quit browser
driver.quit()