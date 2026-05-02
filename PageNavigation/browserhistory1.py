
from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# GET URL
driver.get("https://demo.guru99.com/test/login.html#")
driver.get("https://lalbaugcharaja.com/en/")

# back and forward
driver.back()
driver.forward()