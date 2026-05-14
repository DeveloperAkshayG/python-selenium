""""
This script demonstrates combination of implicit and explicit wait
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://proleed.academy/exercises/selenium/automation-practice-form-with-radio-button-check-boxes-and-drop-down.php")
driver.maximize_window()

# implicit wait for text box
driver.implicitly_wait(10)

# locator for mothername textbox
mothername_locator=driver.find_element(By.ID,"mothername")

# enter input
mothername_locator.send_keys("devki")
time.sleep(2)

# clear input
mothername_locator.clear()
time.sleep(2)

# explicit wait
wait=WebDriverWait(driver,20)

# voter card checkbox locator
votercard_locator=wait.until(expected_conditions.visibility_of_element_located((By.ID,"votercard")))

# click checkbox
votercard_locator.click()
time.sleep(3)

# uncheck the checkbox
votercard_locator.click()
time.sleep(3)

# quit the browser
driver.quit()