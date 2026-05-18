"""
This script demonstrates how to move slider with click() and move_to_element_with_offset method
"""
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# instantiate driver
driver = webdriver.Chrome()

# open url
driver.get("https://jqueryui.com/slider/")
driver.maximize_window()

# implicit wait
driver.implicitly_wait(20)

# switch to iframe
iframe_element = driver.find_element(By.CLASS_NAME, "demo-frame")

# switch to iframe
driver.switch_to.frame(iframe_element)

# slider locator
slider_locator = driver.find_element(By.ID, "slider")

# click on slider
slider_locator.click()
time.sleep(4)

# create instance of actionchains
action = ActionChains(driver)

# move_to_element_with_offset
action.move_to_element_with_offset(slider_locator, -100, 0).click().perform()
time.sleep(4)

# draganddrop
action.drag_and_drop_by_offset(slider_locator,150,0).perform()
time.sleep(4)

# quit browser
driver.quit()
