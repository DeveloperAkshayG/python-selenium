"""
This script returns attribute value of element
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# instantiate chrome driver
driver=webdriver.Chrome()

# open url
driver.get("https://rahulshettyacademy.com/AutomationPractice/#")
driver.maximize_window()
time.sleep(4)

# text box loccator
text_box=driver.find_element(By.ID,"name")

# write value to text box
text_box.send_keys("chintamani")
time.sleep(4)

# find the attribute "value"
print(text_box.get_attribute("value"))

# quit browser
driver.quit()