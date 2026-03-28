import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# open browser
driver=webdriver.Chrome()
time.sleep(2)

# open url
driver.get("https://proleed.academy/exercises/selenium/automation-practice-form-with-radio-button-check-boxes-and-drop-down.php")
driver.maximize_window()
time.sleep(2)

# scroll to specific pixel
driver.execute_script("window.scrollBy(0,300)","")
value=driver.execute_script("return window.pageYOffset;")
print("pixel scrolled are: ", value)
time.sleep(2)

# LOCATE CHECKBOX DRIVING LICENSE
checkbox_locator=driver.find_element(By.ID,"drivinglicense")

# SELECT CHECKBOX
checkbox_locator.click()
time.sleep(3)

#unselect CHECKBOX
checkbox_locator.click()
time.sleep(3)

# LOCATE CHECKBOX VOTER CARD
checkbox_locator=driver.find_element(By.ID,"votercard")

# SELECT CHECKBOX
checkbox_locator.click()
time.sleep(3)

#unselect CHECKBOX
checkbox_locator.click()
time.sleep(3)

# LOCATE CHECKBOX STUDENT ID
checkbox_locator=driver.find_element(By.ID,"studentid")

# SELECT CHECKBOX
checkbox_locator.click()
time.sleep(3)

#unselect CHECKBOX
checkbox_locator.click()
time.sleep(3)


# CLOSE BROWSER
driver.quit()