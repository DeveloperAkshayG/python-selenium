import time

from selenium import webdriver

# instantiate webdriver
driver=webdriver.Chrome()

# open browser
driver.get("https://proleed.academy/exercises/selenium/automation-practice-form-with-radio-button-check-boxes-and-drop-down.php")
driver.maximize_window()
time.sleep(5)

# print title
title=driver.title
print(title)

# assert title
assert title == "Automation Practice Form with Radio Button, Check boxes & Drop-down Menu | Selenium Exercise"

# quit browser
driver.quit()
