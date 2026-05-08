import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# OPEN URL
driver.get("https://proleed.academy/exercises/selenium/automation-practice-form-with-radio-button-check-boxes-and-drop-down.php")
driver.maximize_window()
time.sleep(3)

# scroll complete page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(5)

# scroll to top of page
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
time.sleep(5)

# quit browser
driver.quit()