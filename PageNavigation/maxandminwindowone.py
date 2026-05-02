import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://lalbaugcharaja.com/en/")
driver.maximize_window()
time.sleep(4)
driver.minimize_window()
time.sleep(3)
driver.maximize_window()
time.sleep(4)
driver.minimize_window()
time.sleep(4)

# close browser
driver.quit()