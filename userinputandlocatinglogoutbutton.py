import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# open browser
driver=webdriver.Chrome()
time.sleep(2)

# open url
driver.get("https://admin-demo.nopcommerce.com/admin/")
driver.maximize_window()
time.sleep(2)

# locating username and entering the same
username_locator=driver.find_element(By.ID,"Email")
username_locator.clear()
time.sleep(1)
username_locator.send_keys("admin@yourstore.com")
time.sleep(2)

# locating password and entering the same
password_locator=driver.find_element(By.NAME,"Password")
password_locator.clear()
time.sleep(1)
password_locator.send_keys("admin")
time.sleep(2)

# locating login button and clicking on same
login_locator = driver.find_element(By.XPATH,"//button[@type='submit']")
login_locator.click()
time.sleep(2)

# to get the current url
actual_url=driver.current_url
print(actual_url)

# page contains dashboard
text_locator= driver.find_element(By.XPATH,"//div[@class='content-header']")
actual_text=text_locator.text
print(actual_text)

# locate logout on page
logout_locator= driver.find_element(By.LINK_TEXT,"Logout")
logout_text=logout_locator.text
print(logout_text)