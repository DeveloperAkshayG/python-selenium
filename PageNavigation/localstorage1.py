import time

from selenium import webdriver

# instantiate webdriver
driver=webdriver.Chrome()

# OPEN URL
driver.get("https://demo.guru99.com/test/radio.html")
time.sleep(4)

# set value to local storage for key2
driver.execute_script("window.localStorage.setItem('key2','value34')")
time.sleep(2)

# read the value from local storage
print(driver.execute_script("return window.localStorage.getItem('key2')"))

# close browser
driver.quit()
