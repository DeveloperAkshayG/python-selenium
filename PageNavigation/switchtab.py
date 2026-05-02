import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://lalbaugcharaja.com/en/")
driver.maximize_window()
time.sleep(3)

parent=driver.current_window_handle

# switch to tab
driver.switch_to.new_window("tab")

# open second url
driver.get("https://demo.guru99.com/test/login.html#")
driver.maximize_window()
time.sleep(3)

sec=driver.current_window_handle

# switch to tab1
driver.switch_to.window(parent)
time.sleep(4)

# switch to tab2
driver.switch_to.window(sec)
time.sleep(4)

# close tab2
driver.close()
time.sleep(4)

# quit browser
driver.quit()
