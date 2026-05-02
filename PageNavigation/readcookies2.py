import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://lalbaugcharaja.com/en/")
time.sleep(4)

# read cookies
print(driver.get_cookies())

# close browser
driver.quit()