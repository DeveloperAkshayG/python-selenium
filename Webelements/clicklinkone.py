import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# open browser
driver=webdriver.Chrome()

# open url
driver.get("https://artoftesting.com/samplesiteforselenium#")
driver.maximize_window()
time.sleep(2)

# locate the link to open
link=driver.find_element(By.LINK_TEXT,"Selenium Sample Script")

# CLICK ON LINK
link.click()
time.sleep(3)

# close the browser
driver.quit()