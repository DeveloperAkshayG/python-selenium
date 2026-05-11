"""
This script demonstrates how to get alert text from alert pop up along with implicit wait
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://rahulshettyacademy.com/AutomationPractice/#")
driver.maximize_window()
time.sleep(2)

# implicit wait to find alert element
driver.implicitly_wait(15)

# LOCATOR FOR ALERT ELEMENT
alert_btn=driver.find_element(By.ID,"alertbtn")

# CLICK on alert btn
alert_btn.click()
time.sleep(4)

# switch to alert
alert=driver.switch_to.alert

# get alert text from alert pop up
print("Alert text is -->  ",alert.text)

# accept the alert
alert.accept()
time.sleep(2)

# quit browser
driver.quit()