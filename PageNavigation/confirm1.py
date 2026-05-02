import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://proleed.academy/exercises/selenium/automation-practice-form-with-radio-button-check-boxes-and-drop-down.php")
time.sleep(2)

# trigger confirmation
driver.execute_script("confirm('accept it?')")
time.sleep(3)

# switch to alert
alert_element=driver.switch_to.alert
print(alert_element.text)

# accept alert
alert_element.accept()
time.sleep(3)

# close browser
driver.quit()
