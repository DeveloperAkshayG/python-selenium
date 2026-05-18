"""
This script demonstrates maximized firefox at time browser is launched using chromeoptions
"""
import time

from selenium import webdriver

from selenium.webdriver.common.by import By

firefox_option=webdriver.FirefoxOptions()
firefox_option.add_argument("--start-maximized")

# instantiate driver
driver=webdriver.Firefox(options=firefox_option)

# open url
driver.get("https://rahulshettyacademy.com/AutomationPractice/#")

# implicit wait
driver.implicitly_wait(10)

# locator for checkbox
checkbox_locator=driver.find_element(By.ID,"checkBoxOption2")

# click on checkbox
checkbox_locator.click()
time.sleep(3)
print("checkbox checked...")

# uncheck the checkbox
checkbox_locator.click()
time.sleep(3)
print("checkbox unchecked...")

# quit browser
driver.quit()