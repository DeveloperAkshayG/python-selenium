import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# instantiate chrome driver
driver=webdriver.Chrome()

# OPEN URL
driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(5)

# locate searchbox
search=driver.find_element(By.NAME,"q")

# fill the searchbox
search.send_keys("pankaj udemy")
time.sleep(5)

# get attribute value
print(search.get_attribute("value"))

# close browser
driver.quit()