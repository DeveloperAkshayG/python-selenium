import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options=Options()
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")

# instantiate driver
driver=webdriver.Chrome(options=options)

# open url
driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(2)
print("headless completed!!!")

#quit browser
driver.quit()