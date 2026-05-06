import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# open  url
driver.get("https://www.cricbuzz.com")
driver.maximize_window()
time.sleep(5)

# referesh browser
driver.refresh()
time.sleep(5)

# quit browser
driver.quit()