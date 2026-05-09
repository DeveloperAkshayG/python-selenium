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

# checkbox locator with substring for attribute value contains "mat"
checkbox_locator=driver.find_element(By.CSS_SELECTOR,"input[value*='mat']")

# click on checkbox
checkbox_locator.click()
time.sleep(5)

# unclick checkbox
checkbox_locator.click()
time.sleep(5)

# quit browser
driver.quit()