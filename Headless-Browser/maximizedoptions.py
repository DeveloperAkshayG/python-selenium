"""
This script starts the browser using options
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# instantiate options
options=Options()
options.add_argument("--start-maximized")

# instantiate driver
driver=webdriver.Chrome(options=options)

# open url
driver.get("https://www.cricbuzz.com")
time.sleep(5)

# quit browser
driver.quit()
