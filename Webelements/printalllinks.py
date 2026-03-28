import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# open browser
browser=webdriver.Chrome()
time.sleep(2)

# open url
browser.get("https://proleed.academy/exercises/selenium/automation-practice-form-with-radio-button-check-boxes-and-drop-down.php")
browser.maximize_window()
time.sleep(2)

# find total number of links
link_count=browser.find_elements(By.TAG_NAME,"a")
print(len(link_count))

# print all the link names
for link in link_count:
    print(link.text)

