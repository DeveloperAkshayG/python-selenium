"""
This script demonstrates implicit wait
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://proleed.academy/exercises/selenium/automation-practice-form-with-radio-button-check-boxes-and-drop-down.php")
driver.maximize_window()

# IMPLICIT WAIT
driver.implicitly_wait(20)

# DOB MONTH LOCATOR
dob_month_locator=driver.find_element(By.ID,"dob_month")

# create instance of select class
drop=Select(dob_month_locator)

# select by visible text
drop.select_by_visible_text("September")
time.sleep(3)

# print selected option
print("the selected option is -->  ", drop.first_selected_option.text)

# quit browser
driver.quit()