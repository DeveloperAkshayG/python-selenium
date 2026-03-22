import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# open browser using webdriver interface
driver=webdriver.Chrome()
time.sleep(2)

# open url
driver.get("https://demoqa.com/buttons")
driver.maximize_window()
time.sleep(3)

# locate element for right click
target_element=driver.find_element(By.ID,"rightClickBtn")

# performing right click action
act=ActionChains(driver)
time.sleep(2)

act.context_click(target_element).perform()