import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# open url1
driver.get("https://lalbaugcharaja.com/en/")
driver.maximize_window()
time.sleep(2)

parent_window=driver.current_window_handle

# open new window
driver.switch_to.new_window("window")

# open url2
driver.get("https://www.cricbuzz.com")
driver.maximize_window()
time.sleep(2)
sec_window=driver.current_window_handle

# switch to window1
driver.switch_to.window(parent_window)
time.sleep(3)

# switch to window2
driver.switch_to.window(sec_window)
time.sleep(3)

# close browser
driver.quit()