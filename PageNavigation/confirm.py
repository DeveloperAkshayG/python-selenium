import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# OPEN URL
driver.get("https://chinchpoklichachintamani.com/Mar/index.php")
driver.maximize_window()
time.sleep(4)

# trigger confirmation box
driver.execute_script("confirm('Do you know chintamani?')")
time.sleep(4)

# switch to alert
alert_element=driver.switch_to.alert
print(alert_element.text)

# accept alert
alert_element.accept()
time.sleep(2)

# quit browser
driver.quit()