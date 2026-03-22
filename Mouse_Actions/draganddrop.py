import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
time.sleep(2)

driver.get("https://artoftesting.com/samplesiteforselenium#")
driver.maximize_window()
time.sleep(2)

source_locator=driver.find_element(By.ID,"myImage")
destination_locator=driver.find_element(By.ID,"targetDiv")

act=ActionChains(driver)

act.drag_and_drop(source_locator,destination_locator).perform()
time.sleep(5)

driver.quit()