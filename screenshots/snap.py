import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://www.cricbuzz.com")
driver.maximize_window()
time.sleep(5)

# take screenshot
driver.get_screenshot_as_file("cricbuzz.png")
time.sleep(2)

# quit browser
driver.quit()