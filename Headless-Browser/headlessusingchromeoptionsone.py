import time

from selenium import webdriver

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--window-size=1920,1080")

# instantiate driver
driver=webdriver.Chrome(options=chrome_options)

# open url
driver.get("https://demo.guru99.com/test/radio.html")
driver.maximize_window()
time.sleep(3)
driver.minimize_window()
time.sleep(3)
driver.maximize_window()
time.sleep(3)
driver.refresh()
time.sleep(3)
print("completed!!!!")

# quit browser
driver.quit()