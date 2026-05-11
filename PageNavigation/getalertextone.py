"""
This script gets the alert text from alert pop up
"""
import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://chinchpoklichachintamani.com/Mar/index.php")
driver.maximize_window()
time.sleep(2)

# trigger alert msg
driver.execute_script("alert('you are on best place on earth')")
time.sleep(3)

# switch to alert
alert=driver.switch_to.alert

# print alert text
print("alert text is --> ",alert.text)

# accept the alert
alert.accept()
time.sleep(3)

# quit browser
driver.quit()