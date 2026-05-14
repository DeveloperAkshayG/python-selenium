"""
This script demonstrates implicit wait
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# instantiate webdriver
driver=webdriver.Chrome()

# open url
driver.get("https://artoftesting.com/samplesiteforselenium#")
driver.maximize_window()
time.sleep(2)

# implicit wait
driver.implicitly_wait(10)

# checkbox locator
checkbox_element=driver.find_element(By.XPATH,"//input[@class='Performance']")

# CLICK CHECKBOX
checkbox_element.click()
time.sleep(3)

# unclick checkbox
checkbox_element.click()
time.sleep(2)

# quit browser
driver.quit()