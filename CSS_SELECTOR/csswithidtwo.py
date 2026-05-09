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

# checkbox locator for checkbox2
checkbox_element=driver.find_element(By.CSS_SELECTOR,"#checkBoxOption2")

# click checkbox
checkbox_element.click()
time.sleep(5)

# unclick checkbox
checkbox_element.click()
time.sleep(5)

# quit browser
driver.quit()