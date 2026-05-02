import time

from selenium import webdriver

# instantiate webdriver
driver=webdriver.Chrome()

# open url
driver.get("https://demoqa.com/broken")
time.sleep(4)

# write to local storage for key hamza
driver.execute_script("window.localStorage.setItem('hamza','mazARI')")

# READ THE VALUE FOR KEY 'HAMZA'
print(driver.execute_script("return window.localStorage.getItem('hamza')"))