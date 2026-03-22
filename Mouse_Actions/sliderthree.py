import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# open browser
driver=webdriver.Chrome()
time.sleep(2)

# open url
driver.get("https://www.w3schools.com/howto/howto_js_rangeslider.asp")
driver.maximize_window()
time.sleep(2)

# locate slider
slider_locator=driver.find_element(By.ID,"id2")
print("Before dragging value is: ", slider_locator.get_attribute("value"))

# perform slider drag and drop
act = ActionChains(driver)
act.drag_and_drop_by_offset(slider_locator,20,0).perform()
print("After dragging value is: ", slider_locator.get_attribute("value"))
time.sleep(5)

act.drag_and_drop_by_offset(slider_locator,-30,0).perform()
print("After second dragging value is: ", slider_locator.get_attribute("value"))
time.sleep(5)

