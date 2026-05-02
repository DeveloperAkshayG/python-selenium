import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://chinchpoklichachintamani.com/Mar/index.php")
driver.maximize_window()
time.sleep(3)

# generate alert
driver.execute_script("alert('chinchpoklicha chintamani')")
time.sleep(4)

# switch to alert
alert_element=driver.switch_to.alert
print(alert_element.text)
time.sleep(3)

# accept alert
alert_element.accept()