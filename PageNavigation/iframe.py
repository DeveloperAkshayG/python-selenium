import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# instantiate browser
driver=webdriver.Chrome()

# get url
driver.get("https://demoqa.com/frames")
driver.maximize_window()
time.sleep(3)

# iframe element
iframe_element=driver.find_element(By.ID,"frame1")

# switch to iframe
driver.switch_to.frame(iframe_element)

# find element of interest i.e This is a sample page
element_of_interest=driver.find_element(By.ID,"sampleHeading")
print(element_of_interest.text)
print(element_of_interest.tag_name)

# switch to main content
driver.switch_to.default_content()
print(driver.title)
time.sleep(3)

# quit browser
driver.quit()
