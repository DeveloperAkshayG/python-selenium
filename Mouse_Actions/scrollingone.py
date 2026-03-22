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

# scroll element into view
target_locator=driver.find_element(By.XPATH,"//input[@class='slider-square']")
driver.execute_script("window.scrollBy(0,300)")
value=driver.execute_script("return window.pageYOffset;")
print("pixels dragged are: ",value)

# print slider value
print("the slider value is: ",target_locator.get_attribute("value"))

act=ActionChains(driver)

# drag the slider
act.drag_and_drop_by_offset(target_locator,60,0).perform()
print("the slider value is: ",target_locator.get_attribute("value"))
time.sleep(4)

# close browser
driver.quit()