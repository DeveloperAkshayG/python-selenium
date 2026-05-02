import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://demo.guru99.com/test/login.html#")
driver.maximize_window()
time.sleep(2)

# generate alert
driver.execute_script("alert('Hey! login form opened!')")
time.sleep(4)

# switch to alert
alert=driver.switch_to.alert
print(alert.text)

# accept the alert
alert.accept()

# close browser
driver.quit()

