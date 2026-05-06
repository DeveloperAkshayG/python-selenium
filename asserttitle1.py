import time

from selenium import webdriver

# instantiate webdriver
driver=webdriver.Chrome()

# open url
driver.get("https://demo.guru99.com/test/login.html#")
driver.maximize_window()
time.sleep(5)

# get title
title=driver.title
print(title)

# assert title
assert title == "Login Page"

# close browser
driver.quit()