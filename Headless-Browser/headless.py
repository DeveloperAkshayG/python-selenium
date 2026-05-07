"""
This script demonstrates headless browser using Options
"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# options to add headless
options = Options()
options.add_argument("--headless=new")          # latest headless mode
# options.add_argument("--window-size=1920,1080") # required for headless stability

# instantiate driver
driver=webdriver.Chrome(options=options)

# open url
driver.get("https://www.cricbuzz.com")
time.sleep(2)
