import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://demoqa.com/frames")
time.sleep(2)

# iframe element
iframe_element=driver.find_element(By.ID,"frame2")

# switch to iframe
driver.switch_to.frame(iframe_element)

# element of interest
element_of_interest=driver.find_element(By.ID,"sampleHeading")

#PRINT THE TEXT
print(element_of_interest.text)

# switch to default content
driver.switch_to.default_content()

# quit browser
driver.quit()