"""
This script demonstrates css selector for substrings or contains
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://rahulshettyacademy.com/AutomationPractice/#")
driver.maximize_window()
time.sleep(5)

# css selector for substring with attribute value containing "Ale"
ele_locator=driver.find_element(By.CSS_SELECTOR,"input[value*='Ale']")

# click on alert button
ele_locator.click()
time.sleep(5)

# accept alert
alert=driver.switch_to.alert

# accept alert
alert.accept()
time.sleep(5)

# quit browser
driver.quit()
