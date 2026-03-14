import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# open browser
driver=webdriver.Chrome()
time.sleep(3)

# open webpage
driver.get("https://demo.guru99.com/test/login.html#")
driver.maximize_window()
time.sleep(3)

# locator for email address
driver.find_element(By.ID,"email")

# locator for password
driver.find_element(By.NAME,"passwd")

# locator for sign in button
driver.find_element(By.XPATH,"//button[@id='SubmitLogin']")