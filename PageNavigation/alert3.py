import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://rahulshettyacademy.com/AutomationPractice/#")
driver.maximize_window()
time.sleep(2)

# trigger alert
driver.execute_script("alert('alert! alert! alert!....')")
time.sleep(3)

# switch to alert
alert_element=driver.switch_to.alert
print(alert_element.text)

# accept alert
alert_element.accept()
time.sleep(2)

# close browser
driver.quit()

