"""
This script captures element screenshot using screenshot() method
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://lalbaugcharaja.com/en/")
driver.maximize_window()
time.sleep(4)

# element locator
ele=driver.find_element(By.ID,"media_image-11")

# capture ele screenshot
ele.screenshot("lalbaugcharaja.png")

# quit browser
driver.quit()