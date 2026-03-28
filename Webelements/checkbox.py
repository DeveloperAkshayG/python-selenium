import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# open browser
driver=webdriver.Chrome()

# open url
driver.get("https://artoftesting.com/samplesiteforselenium#")
driver.maximize_window()
time.sleep(2)

# locate checkbox
checkbox=driver.find_elements(By.XPATH,"//input[@type='checkbox']")

#printing total number of checkbox
print("total checkboxes are : ",len(checkbox))

# iterating through checkbox and selecting them using approach 1
for i in range(len(checkbox)):
    checkbox[i].click()
    time.sleep(2)
    checkbox[i].click()
    time.sleep(2)

# iterating through checkbox and selecting them using approach 2
for check in checkbox:
    check.click()
    time.sleep(2)
    check.click()
    time.sleep(2)

# selecting checkbox based on attribute
for check in checkbox:
    choice=check.get_attribute('value')
    if  choice == 'Performance':
        check.click()
        time.sleep(2)
        check.click()
        time.sleep(2)

# selecting first checkbox
for i in range(0,len(checkbox)-1):
    # logic for selecting first checkbox
    checkbox[i].click()
    time.sleep(2)
    checkbox[i].click()
    time.sleep(2)

# selecting only first checkbox
for i in range(len(checkbox)):
    if i < 1:
        # automation checkbox should get selected
        checkbox[i].click()
        time.sleep(2)
        checkbox[i].click()
        time.sleep(2)

# selecting all the checkbox
for check in checkbox:
    check.click()
    time.sleep(2)

# unselecting all the checkbox
for check in checkbox:
    if check.is_selected():
        check.click()
        time.sleep(2)

# close browser
driver.quit()

