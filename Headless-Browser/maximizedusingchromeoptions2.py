import time

from selenium import webdriver

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--window-size=1920,1080")

# instantiate driver
driver=webdriver.Chrome(options=chrome_options)

# open url
driver.get("https://lalbaugcharaja.com/en/")
time.sleep(3)

# quit browser
driver.quit()