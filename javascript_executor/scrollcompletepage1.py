import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://proleed.academy/exercises/selenium/automation-practice-form-with-radio-button-check-boxes-and-drop-down.php")
driver.maximize_window()
time.sleep(2)

# scroll to bottom page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(4)

# scroll to top of page
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
time.sleep(4)

# quit browser
driver.quit()