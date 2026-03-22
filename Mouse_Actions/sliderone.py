import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# open browser
driver=webdriver.Chrome()
time.sleep(2)

#open url
driver.get("https://letcode.in/slider")
driver.maximize_window()
time.sleep(2)

slider_locator=driver.find_element(By.ID,"generate")

print(slider_locator.location)
print("before dragging value is:", slider_locator.get_attribute("value"))

# drag and drop the slider
act=ActionChains(driver)

act.drag_and_drop_by_offset(slider_locator,25,0).perform()
time.sleep(5)
print(slider_locator.location)
print("after dragging value is:", slider_locator.get_attribute("value"))