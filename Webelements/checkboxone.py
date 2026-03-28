import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# open browser using webdriver interface
driver=webdriver.Chrome()
time.sleep(2)

# open url
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(2)

# checkbox locator to find total number of checkbox
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkboxes))

# select and unselect checkbox using for loop
for i in range(len(checkboxes)):
    checkboxes[i].click()
    time.sleep(2)
    checkboxes[i].click()
    time.sleep(2)

# approach 2 for select and unselect checkbox using for loop
for mycheck in checkboxes:
    mycheck.click()
    time.sleep(2)
    mycheck.click()
    time.sleep(2)

# select checkbox based on choice
for mycheck in checkboxes:
    choice=mycheck.get_attribute('id')
    if choice == 'checkBoxOption2' or choice == 'checkBoxOption3':
        mycheck.click()
        time.sleep(2)
        mycheck.click()
        time.sleep(2)

# select last two checkbox
for i in range(len(checkboxes)-2,len(checkboxes)):
    checkboxes[i].click()
    time.sleep(3)
    checkboxes[i].click()
    time.sleep(3)

# select first two checkboxes
for i in range(len(checkboxes)):
    if i<2:
        checkboxes[i].click()
        time.sleep(2)
        checkboxes[i].click()
        time.sleep(2)
        
# selecting all checkboxes and unselecting all
for i in range(len(checkboxes)):
    checkboxes[i].click()
    time.sleep(2)
    
# unselecting the checkboxes
for i in range(len(checkboxes)):
    if checkboxes[i].is_selected():
        checkboxes[i].click()
        time.sleep(2)