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

# scroll down the browser
browser.execute_script("window.scrollBy(0,4000)","")
time.sleep(2)

# locate the link
link=browser.find_element(By.LINK_TEXT,"Selenium Element Locators Practice Form")

# click on link
link.click()
time.sleep(3)

# close browser
browser.quit()