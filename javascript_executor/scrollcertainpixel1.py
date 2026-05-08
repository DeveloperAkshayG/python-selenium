import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://proleed.academy/exercises/selenium/automation-practice-form-with-radio-button-check-boxes-and-drop-down.php")
driver.maximize_window()
time.sleep(5)

# scroll to location (0,1000)
driver.execute_script("window.scrollBy(0,1000)")
time.sleep(4)

# quit browser
driver.quit()