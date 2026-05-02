"""
Another example of switching between 2 windows
"""
import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# open url1
driver.get("https://chinchpoklichachintamani.com/Mar/index.php")
driver.maximize_window()
time.sleep(2)

# current window handle for url1
parent_window=driver.current_window_handle

# switch to window 2 to open new url
driver.switch_to.new_window('window')

# open url2
driver.get("https://lalbaugcharaja.com/en/")
driver.maximize_window()
time.sleep(2)

sec_window=driver.current_window_handle

# switch to parent window
driver.switch_to.window(parent_window)
time.sleep(4)

# switch to new window
driver.switch_to.window(sec_window)
time.sleep(4)

# close browser
driver.quit()