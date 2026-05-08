import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# instantiate driver
driver=webdriver.Chrome()

# OPEN URL
driver.get("https://proleed.academy/exercises/selenium/automation-practice-form-with-radio-button-check-boxes-and-drop-down.php")
driver.maximize_window()
time.sleep(4)

# element locator
ele_locator=driver.find_element(By.ID,"country")
print(ele_locator.text)

# scroll to ele_locator
driver.execute_script("arguments[0].scrollIntoView()",ele_locator)
time.sleep(5)

# quit browser
driver.quit()