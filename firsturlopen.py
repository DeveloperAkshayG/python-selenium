import time

from selenium import webdriver

# open browser using python selenium
mydriver = webdriver.Chrome()
time.sleep(5)

# open url or web page
mydriver.get("https://www.cricbuzz.com")
time.sleep(10)
