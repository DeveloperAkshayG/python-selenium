import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# open browser
driver=webdriver.Chrome()

# open url
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(2)

# locate dropdown
dropdown=driver.find_element(By.ID,"dropdown-class-example")

# create object of select class and pass dropdown as argument to perform dropdown operations
mysel=Select(dropdown)

# selection based on visible text
mysel.select_by_visible_text("Option1")
time.sleep(2)
mysel.select_by_visible_text("Option2")
time.sleep(2)
mysel.select_by_visible_text("Option3")
time.sleep(2)
mysel.select_by_visible_text("Select")
time.sleep(2)

# selection based on value
mysel.select_by_value("option1")
time.sleep(2)
mysel.select_by_value("option2")
time.sleep(2)
mysel.select_by_value("option3")
time.sleep(2)
mysel.select_by_value("")
time.sleep(2)

# selection based on index
mysel.select_by_index(1)
time.sleep(2)
mysel.select_by_index(2)
time.sleep(2)
mysel.select_by_index(3)
time.sleep(2)
mysel.select_by_index(0)
time.sleep(2)

# print total number of options available
myopt=mysel.options
print("the total dropdown options are: ",len(myopt))

# selecting value without built in method
for opt in myopt:
    if opt.text == "Option2":
        opt.click()
        time.sleep(2)

# locating dropdown using xpath
mydrop=driver.find_elements(By.XPATH,"//select[@id='dropdown-class-example']/option")
print(len(mydrop))
