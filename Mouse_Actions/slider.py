import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# open browser
driver=webdriver.Chrome()
time.sleep(2)

#open url
driver.get("https://demoqa.com/slider")
driver.maximize_window()
time.sleep(2)

# locate slider
#slider_locator=driver.find_element(By.XPATH,"//input[@type='range']")
slider_locator=driver.find_element(By.ID,"slider")
time.sleep(2)

#print(slider_locator.location)  # {'x': 246, 'y': 223}
print("Before dragging value:", slider_locator.get_attribute("value"))


# perform slider action
act=ActionChains(driver)

act.drag_and_drop_by_offset(slider_locator,100,0).perform()
#print(slider_locator.location)
print("After dragging value:", slider_locator.get_attribute("value"))
time.sleep(5)