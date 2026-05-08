import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://rahulshettyacademy.com/AutomationPractice/#")
driver.maximize_window()
time.sleep(5)

# scroll to bottom of page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(5)

# scroll to top of page
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
time.sleep(5)

# quit browser
driver.quit()