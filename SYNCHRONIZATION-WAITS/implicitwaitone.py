"""
This script demonstrates implicit wait in selenium
"""
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# instantiate driver
driver=webdriver.Chrome()

# OPEN URL
driver.get("https://rahulshettyacademy.com/AutomationPractice/#")
time.sleep(2)

# implicit wait
driver.implicitly_wait(10)

# locator for mouse over
hover=driver.find_element(By.ID,"mousehover")

# create instance of action class
act=ActionChains(driver)

# mouse hover over element
act.move_to_element(hover).perform()
time.sleep(2)

# quit browser
driver.quit()