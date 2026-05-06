"""
This script captures the screenshot of the particular element on page
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# instantiate the driver
driver=webdriver.Chrome()

# open url
driver.get("https://chinchpoklichachintamani.com/Mar/index.php")
driver.maximize_window()
time.sleep(2)

# locate element
element=driver.find_element(By.ID,"org_name")
time.sleep(2)

# capture element screenshot
element.screenshot("element.png")

# quit browser
driver.quit()