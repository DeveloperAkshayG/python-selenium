"""
This script demonstrates how to apply implicit wait rather than using time.sleep(2) with find_element
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# instantitate driver
driver=webdriver.Chrome()

# open url
driver.get("https://artoftesting.com/samplesiteforselenium#")
time.sleep(2)

# implicit wait
driver.implicitly_wait(10)

# locator for dropdown
drop=driver.find_element(By.ID,"testingDropdown")

# create instance of select class
mydrop=Select(drop)

# select by value
mydrop.select_by_value("Manual")
time.sleep(3)

# quit browser
driver.quit()