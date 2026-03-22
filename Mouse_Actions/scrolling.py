import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# open browser using webdriver interface
driver=webdriver.Chrome()
time.sleep(2)

# open url
driver.get("https://artoftesting.com/samplesiteforselenium#")
driver.maximize_window()
time.sleep(1)

# scroll random pixel
driver.execute_script("window.scrollBy(0,1500)","")
value=driver.execute_script("return window.pageYOffset;")
print("pixels scrolled are: ", value)
time.sleep(3)

# scroll back to start
driver.execute_script("window.scrollBy(0,-1500)","")
value=driver.execute_script("return window.pageYOffset;")
print("pixels scrolled are: ", value)
time.sleep(3)

# scroll to certain element in view
target_locator=driver.find_element(By.ID,"myImage")
driver.execute_script("arguments[0].scrollIntoView();",target_locator)
value=driver.execute_script("return window.pageYOffset;")
print("pixels scrolled are: ", value)
time.sleep(3)

# scroll to start of page
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("pixels are: ",value)
time.sleep(3)

# scroll to bottom of page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("pixels are: " , value)
time.sleep(3)

# close browser
driver.quit()