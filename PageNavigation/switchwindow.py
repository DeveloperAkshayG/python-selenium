import time

from selenium import webdriver

driver=webdriver.Chrome()

# open url 1
driver.get("https://www.cricbuzz.com")
driver.maximize_window()
time.sleep(3)

cricbuzz_window=driver.current_window_handle

# open new window
driver.switch_to.new_window('window')

# open url 2
driver.get("https://www.youtube.com")
driver.maximize_window()
time.sleep(3)

# switch to cricbuzz
driver.switch_to.window(cricbuzz_window)
time.sleep(3)

# quit browser
driver.quit()