"""
This script captures the screenshot of the current open page
"""
import time

from selenium import webdriver

# instantiate the driver
driver=webdriver.Chrome()

# open url
driver.get("https://chinchpoklichachintamani.com/Mar/index.php")
driver.maximize_window()
time.sleep(2)

# taking screenshot of page
driver.save_screenshot("test.png")
time.sleep(2)

# quit browser
driver.quit()