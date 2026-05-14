"""
This script demonstrates how to setup explicit wait in selenium
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
wait= WebDriverWait(driver,20)
wait.until(expected_conditions.visibility_of(driver.find_element(By.XPATH,"//input[@value='radio2']")))

# locator for radio2
radio2=driver.find_element(By.XPATH,"//input[@value='radio2']")

# click radio button
radio2.click()
time.sleep(3)

# quit browser
driver.quit()