import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# instantiate chrome driver
driver=webdriver.Chrome()

# open url
driver.get("https://github.com/login")
driver.maximize_window()
time.sleep(4)

# locate element of interest
element_interest= driver.find_element(By.LINK_TEXT,"Create an account")
print("text is --->  ", element_interest.text)
test_text=element_interest.text

#  test the particular condition
assert "account" in test_text, "value not found"
assert "accountee" in test_text, "value not found"


# quit browser
driver.quit()