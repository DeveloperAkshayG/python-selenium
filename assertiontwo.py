import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# open browser
driver= webdriver.Chrome()
time.sleep(2)

# open url
driver.get("https://admin-demo.nopcommerce.com/login?returnUrl=%2Fadmin%2F")
driver.maximize_window()
time.sleep(2)

# locating username and entering the same
username_locator=driver.find_element(By.ID,"Email")
username_locator.clear()
time.sleep(1)
username_locator.send_keys("admin@yourstore.com")
time.sleep(1)

# locating password and entering the same
password_locator=driver.find_element(By.ID,"Password")
password_locator.clear()
time.sleep(1)
password_locator.send_keys("admin")
time.sleep(1)

# locating login button and clicking on same
login_locator=driver.find_element(By.XPATH,"//button[@type='submit']")
login_locator.click()
time.sleep(1)

# getting the current url and comparing with expected using assertion
actual_url=driver.current_url
assert actual_url == "https://admin-demo.nopcommerce.com/admin/"

# verifying page contains Dashboard and verifying it using assertion
text_to_search=driver.find_element(By.XPATH,"//div[@class='content-header']")
actual_text=text_to_search.text
assert actual_text == "Dashboard"

# verfying logout button is present using assert
logout_locator=driver.find_element(By.LINK_TEXT,"Logout")
assert logout_locator.is_displayed()