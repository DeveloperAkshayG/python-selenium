import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# OPEN URL1
driver.get("https://www.cricbuzz.com")
driver.maximize_window()
time.sleep(2)

parent=driver.current_window_handle

# open new window
driver.switch_to.new_window("window")

# open url2
driver.get("https://demo.guru99.com/test/radio.html")
driver.maximize_window()
time.sleep(2)

sec=driver.current_window_handle

# switch to window1
driver.switch_to.window(parent)
time.sleep(4)

# switch to window2
driver.switch_to.window(sec)
time.sleep(4)

# close window2
driver.close()
time.sleep(4)

# close browser
driver.quit()