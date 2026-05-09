"""
This script demonstrates css selector for substrings or contains
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

# text box locator for substrings for textbox containing  stNa
textbox=driver.find_element(By.CSS_SELECTOR,"input[name*='stNa']")

# entering input to textbox
textbox.send_keys("Ryan")
time.sleep(5)

# clear textbox
textbox.clear()
time.sleep(5)

# quit browser
driver.quit()
