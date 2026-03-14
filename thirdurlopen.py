import time

from selenium import webdriver

# open browser
drive=webdriver.Chrome()
time.sleep(5)

# open web page
drive.get("https://lalbaugcharaja.com/en/")
drive.maximize_window()
time.sleep(5)
