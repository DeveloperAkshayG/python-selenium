"""
This script demonstrates maximized option using chrome options
"""
import time

from selenium import webdriver

# INSTANTIATE CHROMEOPTIONS
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")

# instantiate driver
driver=webdriver.Chrome(options=chrome_options)

# open url
driver.get("https://www.cricbuzz.com")
time.sleep(5)

# quit browser
driver.quit()