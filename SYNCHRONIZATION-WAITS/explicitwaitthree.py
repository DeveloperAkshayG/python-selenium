"""
This script demonstrate explicit wait
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://proleed.academy/exercises/selenium/automation-practice-form-with-radio-button-check-boxes-and-drop-down.php")
driver.maximize_window()

#locator for prefix dropdown with explicit wait
wait=WebDriverWait(driver,20)
prefix_dropdown=wait.until(expected_conditions.visibility_of(driver.find_element(By.ID,"prefix")))

# create instance of alert
mydrop=Select(prefix_dropdown)

# select by visible text
mydrop.select_by_visible_text("Ms.")
time.sleep(3)

# quit browser
driver.quit()