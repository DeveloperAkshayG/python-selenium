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

# instantiate webdriver
driver=webdriver.Chrome(options=options)

# get url
driver.get("https://lalbaugcharaja.com/en/")
driver.maximize_window()
time.sleep(3)
driver.minimize_window()
time.sleep(3)
driver.maximize_window()
time.sleep(3)
driver.minimize_window()
time.sleep(3)
driver.minimize_window()
time.sleep(3)