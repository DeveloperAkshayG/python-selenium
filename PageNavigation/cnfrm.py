import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# get url
driver.get("https://lalbaugcharaja.com/en/")
time.sleep(3)

# trigger confirmation box
driver.execute_script("confirm('do you want to confirm?')")
time.sleep(3)

# switch to confirm box
alert_ele=driver.switch_to.alert
print(alert_ele.text)

# accept alert
alert_ele.dismiss()
time.sleep(4)

# quit browser
driver.quit()

