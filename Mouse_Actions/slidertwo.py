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

# loccate slider
slider_locator=driver.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[1]/div[1]/div[3]/input")
time.sleep(2)

# perform drag and drop slider
act = ActionChains(driver)

print("Before dragging value is: ", slider_locator.get_attribute("value"))

act.drag_and_drop_by_offset(slider_locator,20,0).perform()
time.sleep(5)
print("After dragging value is: ", slider_locator.get_attribute("value"))

driver.quit()