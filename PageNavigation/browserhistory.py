"""
This script demosntrates back and forward commands used in selenium
"""
import time

from selenium import webdriver

# isntantiate webdriver
driver=webdriver.Chrome()

# get url
driver.get("https://demo.guru99.com/test/login.html#")
time.sleep(2)
driver.get("https://www.cricbuzz.com")
time.sleep(2)

# back command
driver.back()


driver.back()


# forward command
driver.forward()
