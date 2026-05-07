import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# instantiate driver for chrome
driver=webdriver.Chrome()

# OPEN URL
driver.get("https://chinchpoklichachintamani.com/Mar/index.php")
time.sleep(5)

# element locator
ele=driver.find_element(By.ID,"org_name")

# ELEMENT SCREENSHOT
ele.screenshot("element.png")

# quit browser
driver.quit()