import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://lalbaugcharaja.com/en/")
driver.maximize_window()
time.sleep(5)

# target element
target_element=driver.find_element(By.LINK_TEXT,"Lalbaughcharaja Live")

# scroll till element into view
driver.execute_script("arguments[0].scrollIntoView();",target_element)
time.sleep(5)

# quit browser
driver.quit()