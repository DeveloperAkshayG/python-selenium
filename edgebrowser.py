import time

from selenium import webdriver

# instantiate driver for edge
driver=webdriver.Edge()

# OPEN url
driver.get("https://www.cricbuzz.com")
driver.maximize_window()
time.sleep(5)

# open another url
driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(5)

# navigate back
driver.back()
time.sleep(5)

# referesh  browser
driver.refresh()
time.sleep(5)

# navigate forward
driver.forward()
time.sleep(5)

# close browser
driver.quit()