"""
This script demonstrates css selector locator endswith
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

# element locator for text box for attribute placeholder ends with r Name
textbox=driver.find_element(By.CSS_SELECTOR,"input[placeholder$='r Name']")

# enter input
textbox.send_keys("Chintamani")
time.sleep(5)

# clear input
textbox.clear()
time.sleep(5)

# quit browser
driver.quit()

