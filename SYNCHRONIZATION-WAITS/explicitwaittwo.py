"""
This script demonstrates how to use explicit wait
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://rahulshettyacademy.com/AutomationPractice/#")
driver.maximize_window()

# explicit wait
wait=WebDriverWait(driver,15)
confirm_btn=wait.until(expected_conditions.visibility_of_element_located((By.ID,"confirmbtn")))

# click on confirm btn
confirm_btn.click()
time.sleep(3)

# switch to alert
alert=driver.switch_to.alert

# accept the alert
alert.accept()
time.sleep(3)

# quit browser
driver.quit()