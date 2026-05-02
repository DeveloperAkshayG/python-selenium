import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://demo.guru99.com/test/login.html#")
time.sleep(5)

# print size
print("size:",driver.get_window_size())

# set size
driver.set_window_size(1100,750)
time.sleep(4)

print("size:",driver.get_window_size())

# get window position
print("position:",driver.get_window_position())

# set position
driver.set_window_position(15,15)
print("position:",driver.get_window_position())


# get window coordinates
print("coordinates:",driver.get_window_rect())

# set coordinates
driver.set_window_rect(20,15,1200,800)

print("coordinates:",driver.get_window_rect())


# close browser
driver.quit()