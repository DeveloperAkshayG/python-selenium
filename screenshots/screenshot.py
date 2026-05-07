"""
This script demonstrate taking screenshot using save_screenshot
"""
import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://chinchpoklichachintamani.com/Mar/index.php")
time.sleep(5)

# take screenshot
driver.save_screenshot("chintamani.png")

# quit browser
driver.quit()