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
time.sleep(2)

# locate the element for double click
target_element=driver.find_element(By.ID,"doubleClickBtn")

# perform double click action
act=ActionChains(driver)

act.double_click(target_element).perform()
time.sleep(2)
print("did double click....")