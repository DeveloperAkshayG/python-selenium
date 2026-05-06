import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# OPEN URL
driver.get("https://www.cricbuzz.com")
time.sleep(5)
driver.get("https://www.google.com")
time.sleep(5)

# navigate back to cricbuzz
driver.back()
time.sleep(5)

# referesh browser
driver.refresh()
time.sleep(5)

# navigate forward to google
driver.forward()
time.sleep(5)

# quit browser
driver.quit()