"""
This script demonstrates headless browser using Options
"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# add headless
options=Options()

options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")

# instantiate driver
driver=webdriver.Chrome(options=options)

# open url
driver.get("https://proleed.academy/exercises/selenium/automation-practice-form-with-radio-button-check-boxes-and-drop-down.php")
driver.maximize_window()
time.sleep(4)
driver.minimize_window()
time.sleep(4)

# quit browser
driver.quit()