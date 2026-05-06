"""
    This script demonstrates conditional commands used in selenium
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# open browser
driver=webdriver.Chrome()

# open url
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()
time.sleep(2)

# locate username
username=driver.find_element(By.ID,"username")

# conditional commands
print("the display status is :", username.is_displayed())
print("the enabled status is :", username.is_enabled())
