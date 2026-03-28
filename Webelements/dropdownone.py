import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# open browser
driver=webdriver.Chrome()

# open url
driver.get("https://proleed.academy/exercises/selenium/automation-practice-form-with-radio-button-check-boxes-and-drop-down.php")
driver.maximize_window()
time.sleep(2)

# dropdown locator
drop=driver.find_element(By.ID,"dob_month")

# creating obj of select class and passing drop as argument to it
mydrop=Select(drop)

# selecting the options based on visible text
mydrop.select_by_visible_text("August")
time.sleep(2)

# selecting the options based on index
mydrop.select_by_index(12)
time.sleep(2)

# finding total number of options available and printing them
opt=mydrop.options
print("the total number of options are: ", len(opt))

# printing the options one by one
for myopt in opt:
    print(myopt.text)

# selecting the option without using in-built method
for myopt in opt:
    if myopt.text == 'June':
        myopt.click()
        time.sleep(2)

# finding total number of options and priting them using xpath
myopt=driver.find_elements(By.XPATH,"//select[@id='dob_month']/option")
print(len(myopt))