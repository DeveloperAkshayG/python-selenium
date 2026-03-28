import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# open browser
driver = webdriver.Chrome()

# open url
driver.get("https://proleed.academy/exercises/selenium/automation-practice-form-with-radio-button-check-boxes-and-drop-down.php")
driver.maximize_window()
time.sleep(2)

# scroll to checkbox area
driver.execute_script("window.scrollBy(0,300)", "")
time.sleep(4)

# locating checkbox
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and @name='identity_type[]']")
print(len(checkboxes))

# selecting all checkbox approach1
for i in range(len(checkboxes)):
    checkboxes[i].click()
    time.sleep(4)
    # unselecting checkbox
    checkboxes[i].click()
    time.sleep(4)

# selecting all checkbox approach2
for checkbox in checkboxes:
    checkbox.click()
    time.sleep(4)
    # unselecting checkbox
    checkbox.click()
    time.sleep(4)

# selecting multiple checkbox based on choice
for checkbox in checkboxes:
    choice = checkbox.get_attribute('id')
    if choice == 'studentid' or choice == 'votercard':
        checkbox.click()
        print("choice checkbox selected")
        time.sleep(3)
        checkbox.click()
        time.sleep(2)
    else:
        print('try again till choice is selected')

# selecting last two checkbox
for i in range(len(checkboxes) - 2, len(checkboxes)):
    print("inside last two selection")
    checkboxes[i].click()
    time.sleep(4)
    checkboxes[i].click()
    time.sleep(4)

# selecting first two checkbox
for i in range(len(checkboxes)):
    if i < 2:
        checkboxes[i].click()
        time.sleep(3)
        checkboxes[i].click()
        time.sleep(2)

# selecting all checkbox to clear all the checkbox once
for i in range(len(checkboxes)):
    checkboxes[i].click()
    time.sleep(4)

# clear all checkbox logic
for i in range(len(checkboxes)):
    if checkboxes[i].is_selected():
        checkboxes[i].click()
        time.sleep(4)
