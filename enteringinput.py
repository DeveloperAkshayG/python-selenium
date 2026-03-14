import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# open browser
driver=webdriver.Chrome()
time.sleep(2)

# open url
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()
time.sleep(3)

# locating username and entering the username
username_locator = driver.find_element(By.ID,"username")
username_locator.send_keys("student")
time.sleep(2)

# locating password and entering the password
password_locator= driver.find_element(By.NAME,"password")
password_locator.send_keys("Password123")
time.sleep(2)

# locating submit button and click on same
submit_locator= driver.find_element(By.ID,"submit")
submit_locator.click()
time.sleep(2)