
from selenium import webdriver

# instantiate webdriver
driver=webdriver.Chrome()

# open url
driver.get("https://demo.guru99.com/test/login.html#")

# setitem in local storage
driver.execute_script("window.localStorage.setItem('key1','wipro')")

# read item
print(driver.execute_script("return window.localStorage.getItem('key1')"))

# close browser
driver.quit()