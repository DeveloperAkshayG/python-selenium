import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://www.cricbuzz.com")
time.sleep(5)
print("size is: ",driver.get_window_size())
print("position is: ",driver.get_window_position())
print("cooridnates are: ",driver.get_window_rect())
time.sleep(5)

# close browser
driver.quit()