import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://chinchpoklichachintamani.com/Mar/index.php")
time.sleep(5)

print("size is: " ,driver.get_window_size())

# set window size
driver.set_window_size(2020,1000)
time.sleep(4)

print("size is: " ,driver.get_window_size())

# print postion
print("position is: ",driver.get_window_position())

# set window position
driver.set_window_position(20,20)
time.sleep(4)

print("position is: ",driver.get_window_position())

# window coordinates
print("coordinates: ",driver.get_window_rect())

# set window coordinates
driver.set_window_rect(30,30,1500,850)
time.sleep(5)

print("coordinates: ",driver.get_window_rect())

# close browser
driver.quit()