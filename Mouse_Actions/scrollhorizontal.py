import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# open browser using webdriver interface
driver=webdriver.Chrome()
time.sleep(2)

# open url
driver.get("https://www.w3schools.com/howto/howto_js_rangeslider.asp")
driver.maximize_window()
time.sleep(2)

# scroll to certain pixel
driver.execute_script("window.scrollBy(0,1000)","")
value=driver.execute_script("return window.pageYOffset;")
print("pixels scrolled are:",value)
time.sleep(4)

# scroll back to start
driver.execute_script("window.scrollBy(0,-1000)","")
value=driver.execute_script("return window.pageYOffset;")
print("pixels scrolled are:",value)
time.sleep(4)

# scroll down the page till element is visible
target_locator=driver.find_element(By.ID,"id3")
driver.execute_script("arguments[0].scrollIntoView();",target_locator)
value=driver.execute_script("return window.pageYOffset;")
print("pixels scrolled are:",value)
time.sleep(4)

# scroll to top of page
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("pixels scrolled are: ", value)
time.sleep(3)

# scroll to bottom of page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("pixels scrolled are: ", value)
time.sleep(3)

# scroll to top of page
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffest;")
print("pixels scrolled are : ", value)
time.sleep(4)

# close browser
driver.quit()