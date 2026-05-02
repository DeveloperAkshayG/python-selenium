import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://chinchpoklichachintamani.com/Mar/index.php")
time.sleep(2)

# window handle for parent
parent=driver.current_window_handle

# open new tab
driver.switch_to.new_window("tab")

# open url2
driver.get("https://lalbaugcharaja.com/en/")
time.sleep(2)

# window handle for sec
sec=driver.current_window_handle

# switch to tab1
driver.switch_to.window(parent)
time.sleep(4)

# switch to tab2
driver.switch_to.window(sec)
time.sleep(4)

# close tab2
driver.close()

# switch to parent
driver.switch_to.window(parent)

# quit browser
driver.quit()