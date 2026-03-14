import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# open browser
driver=webdriver.Chrome()
time.sleep(2)

# open url
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()
time.sleep(2)

# locating username and entering the same
username_locator=driver.find_element(By.ID,"username")
username_locator.send_keys("student")
time.sleep(2)

# locating pasword and entering the same
password_locator=driver.find_element(By.NAME,"password")
password_locator.send_keys("Password123")
time.sleep(2)

# click on login button
login_locator=driver.find_element(By.ID,"submit")
#login_locator.click()
#time.sleep(2)

# getting the url and comparing it using assertion
#actual_url= driver.current_url
#print(actual_url)
#assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

# validating page contains logged in successfully using assertion
text_match=driver.find_element(By.TAG_NAME,"h1")
actual_text=text_match.text
assert actual_text == "Logged In Successfully"

# validating page contains logout button using assertion
logout_locator=driver.find_element(By.LINK_TEXT,"Log out")
assert logout_locator.is_displayed()