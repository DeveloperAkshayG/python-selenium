"""
This script demonstrates headless using chrome options
"""
import time

from selenium import webdriver

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--window-size=1920,1080")

# instantiate driver
driver=webdriver.Chrome(options=chrome_options)

# open url
driver.get("https://www.cricbuzz.com")
driver.maximize_window()
time.sleep(2)

# quit browser
driver.quit()
