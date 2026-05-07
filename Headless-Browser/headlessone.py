"""
This script demonstrates headless browser using Options
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# options to add headless
options = Options()

# latest headless mode
options.add_argument("--headless=new")

# window size
options.add_argument("window-size=1920,1080")

# instantiate driver
driver=webdriver.Chrome(options=options)

# OPEN URL
driver.get("https://chinchpoklichachintamani.com/Mar/index.php")
driver.maximize_window()
time.sleep(3)
driver.minimize_window()
time.sleep(3)
driver.maximize_window()
time.sleep(4)
driver.minimize_window()
time.sleep(3)

# quit browser
driver.quit()