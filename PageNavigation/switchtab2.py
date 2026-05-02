import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# OPEN URL1
driver.get("https://www.cricbuzz.com")
time.sleep(2)

parent=driver.current_window_handle

# open new tab
driver.switch_to.new_window("tab")

# open url2
driver.get("https://demo.guru99.com/test/login.html#")
time.sleep(2)

sec=driver.current_window_handle

# switch to tab1
driver.switch_to.window(parent)
time.sleep(4)

# switch to tab2
driver.switch_to.window(sec)
time.sleep(4)

# close tab2
driver.close()
driver.switch_to.window(parent)

# close browser
driver.quit()