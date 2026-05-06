"""
    This script demonstrates close browser command which closes parent browser window
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# open browser
driver=webdriver.Chrome()

# open url
driver.get("https://rahulshettyacademy.com/AutomationPractice/#")
driver.maximize_window()
time.sleep(2)

# locate new tab
tab=driver.find_element(By.ID,"opentab")

# click on tab
tab.click()
time.sleep(3)

# close the browser using close command
driver.close()
time.sleep(3)

# to demonstrate quit command
driver.quit()