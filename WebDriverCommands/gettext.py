"""
This script gets text from element
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# instantiate chrome driver
driver=webdriver.Chrome()

# open url
driver.get("https://demo.guru99.com/test/login.html#")
driver.maximize_window()
time.sleep(5)

# element of interest
element_interest=driver.find_element(By.ID,"SubmitLogin")
print(element_interest.text)

# ASSERT TEXT
test_value=element_interest.text
assert 'in' in test_value

# close browser
driver.quit()