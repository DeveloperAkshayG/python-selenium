"""
    This script demonstrates is_selected() conditional commands used with checkbox and radio
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# open browser
driver=webdriver.Chrome()

# open url
driver.get("https://demo.guru99.com/test/radio.html")
driver.maximize_window()

# locate checkbox and radio
checkbox=driver.find_element(By.ID,"vfb-6-0")
radio1=driver.find_element(By.ID,"vfb-7-1")
radio2=driver.find_element(By.ID,"vfb-7-2")

# is_selected with checkbox
print("checkbox selected status is :" , checkbox.is_selected())
checkbox.click()
time.sleep(2)
print("checkbox selected status is :" , checkbox.is_selected())
time.sleep(2)

# is_selected with radio1
print("radio1 selected status is: ", radio1.is_selected())
print("radio2 selected status is: ", radio2.is_selected())
radio1.click()
time.sleep(2)
print("radio1 selected status is: ", radio1.is_selected())
print("radio2 selected status is: ", radio2.is_selected())
time.sleep(2)

# is_selected with radio2
print("radio1 selected status is: ", radio1.is_selected())
print("radio2 selected status is: ", radio2.is_selected())
radio2.click()
time.sleep(2)
print("radio1 selected status is: ", radio1.is_selected())
print("radio2 selected status is: ", radio2.is_selected())
time.sleep(2)

# close browser
driver.quit()