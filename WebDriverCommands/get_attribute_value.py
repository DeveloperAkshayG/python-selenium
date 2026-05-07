"""
This script gets the attribute value of particular element
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# instantiate chrome driver
driver=webdriver.Chrome()

# OPEN URL
driver.get("https://demo.guru99.com/test/login.html#")
driver.maximize_window()
time.sleep(5)

# locate username
username=driver.find_element(By.ID,"email")

# enter username
username.send_keys("joe123@gmail.com")
time.sleep(5)

# locate attribute value
print(username.get_attribute("name"))

# quit browser
driver.quit()