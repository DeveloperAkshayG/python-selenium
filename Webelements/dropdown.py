import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# open browser
driver=webdriver.Chrome()

# open url
driver.get("https://artoftesting.com/samplesiteforselenium#")
driver.maximize_window()
time.sleep(2)

# locate dropdown
droplocator=driver.find_element(By.ID,"testingDropdown")

# creating a object of Select class and passing droplocator as argument to class
drop=Select(droplocator)

# selecting the option based on text
drop.select_by_visible_text("Manual Testing")
time.sleep(2)
drop.select_by_visible_text("Database Testing")
time.sleep(2)
drop.select_by_visible_text("Automation Testing")
time.sleep(2)
drop.select_by_visible_text("Performance Testing")

# selecting the option based on value

drop.select_by_value("Manual")
time.sleep(2)
drop.select_by_value("Database")
time.sleep(2)
drop.select_by_value("Automation")
time.sleep(2)
drop.select_by_value("Performance")
time.sleep(2)

# selecting the option based on index
drop.select_by_index(0)
time.sleep(2)
drop.select_by_index(1)
time.sleep(2)
drop.select_by_index(2)
time.sleep(2)
drop.select_by_index(3)
time.sleep(2)

# printing total number of options available
option=drop.options
print("the total options are: ",len(option))

# printing the option one by one
for opt in option:
    print(opt.text)

# selecting the option without using built-in method
for opt in option:
    if opt.text == 'Manual Testing':
        opt.click()
        time.sleep(2)

# identifying total xpath using different path
myopt=driver.find_elements(By.XPATH,'//select[@id="testingDropdown"]/option')
print(len(myopt))