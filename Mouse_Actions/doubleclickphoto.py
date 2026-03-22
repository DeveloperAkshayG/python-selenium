import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# open browser
driver=webdriver.Chrome()
time.sleep(2)

#open url
driver.get("https://lalbaugcharaja.com/en/")
driver.maximize_window()
time.sleep(2)

# locate photos on url
target_locator=driver.find_element(By.LINK_TEXT,"Photos")
time.sleep(2)

# perform double click action
act=ActionChains(driver)

act.double_click(target_locator).perform()
time.sleep(2)

# close browser
driver.quit()
