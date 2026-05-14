"""
This script demonstrates explicit wait in selenium
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://artoftesting.com/samplesiteforselenium#")
driver.maximize_window()


# explicit wait
wait=WebDriverWait(driver,15)
wait.until(expected_conditions.visibility_of(driver.find_element(By.ID,"fname")))

# locator for text box
textbox=driver.find_element(By.ID,"fname")

# enter the input
textbox.send_keys("CHINTAMANI")
time.sleep(3)

# clear the input
textbox.clear()
time.sleep(3)

# quit browser
driver.quit()