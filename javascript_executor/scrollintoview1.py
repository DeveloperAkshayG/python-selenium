import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# instantiate driver
driver=webdriver.Chrome()

# OPEN URL
driver.get("https://rahulshettyacademy.com/AutomationPractice/#")
driver.maximize_window()
time.sleep(4)

# element locator for mouse hover
ele_locator=driver.find_element(By.ID,"mousehover")

# scroll element into view
driver.execute_script("arguments[0].scrollIntoView();",ele_locator)
time.sleep(5)

# quit browser
driver.quit()