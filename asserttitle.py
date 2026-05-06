import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(5)

# get title
title=driver.title
print(title)

# assert title
assert title == 'Google'

# close browser
driver.quit()