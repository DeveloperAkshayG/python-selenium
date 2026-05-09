"""
This script demonstrates css selector with id
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://artoftesting.com/samplesiteforselenium#")
driver.maximize_window()
time.sleep(5)

# text box locator
ele_locator=driver.find_element(By.CSS_SELECTOR,"#fname")
print(ele_locator.get_attribute("type"))

# enter input
ele_locator.send_keys("Virat")
time.sleep(5)

# clear text box
ele_locator.clear()
time.sleep(5)

# quit browser
driver.quit()