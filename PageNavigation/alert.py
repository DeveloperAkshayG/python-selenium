"""
This script generates alert and accept the same
"""
import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# OPEN URL
driver.get("https://lalbaugcharaja.com/en/")
driver.maximize_window()
time.sleep(3)

# trigger alert without alert button
driver.execute_script("alert('Hey! Lalbaugcha raja cha vijay aso!')")
time.sleep(4)

# switch to alert
alert=driver.switch_to.alert

# print alert text
print(alert.text)

# accept the alert
alert.accept()
time.sleep(3)

# quit the browser
driver.quit()