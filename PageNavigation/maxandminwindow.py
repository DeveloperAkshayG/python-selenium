import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://www.cricbuzz.com")
time.sleep(5)

# maximizing the window
driver.maximize_window()
time.sleep(4)

# minimizing the window
driver.minimize_window()
time.sleep(4)

# maximizing the window
driver.maximize_window()
time.sleep(4)

# close browser
driver.quit()