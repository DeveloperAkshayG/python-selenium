import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options=Options()
options.add_argument("--start-maximized")
options.add_argument("--window-size=1920,1080")

# instantiate chrome driver
driver=webdriver.Chrome(options=options)

# open url
driver.get("https://lalbaugcharaja.com/en/")
time.sleep(3)

# quit browser
driver.quit()
