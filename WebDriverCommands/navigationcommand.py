import time

from selenium import webdriver

driver=webdriver.Chrome()

driver.get("https://www.cricbuzz.com")
driver.maximize_window()
time.sleep(2)

driver.get("https://lalbaugcharaja.com/en/")
time.sleep(2)

# back navigational command
driver.back()
time.sleep(3)

# forward navigational command
driver.forward()
time.sleep(3)

# referesh navigational command
driver.refresh()
time.sleep(4)

# quit browser
driver.quit()