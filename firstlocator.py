import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# open webdriver
driver = webdriver.Chrome()
time.sleep(3)

# open webpage
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()
time.sleep(3)

# locating username field
driver.find_element(By.ID,"username")

# locating password field
driver.find_element(By.NAME,"password")

# locating submit button
driver.find_element(By.XPATH,"//button[@id='submit']")
