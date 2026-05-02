""""
since this url contains nested iframes , first i had to switch to parent iframe and
then to child iframe
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# instantiate driver
driver=webdriver.Chrome()

# OPEN URL
driver.get("https://demoqa.com/nestedframes")
time.sleep(2)

# locate parent iframe
parent_iframe=driver.find_element(By.ID,"frame1")

# switch to parent iframe
driver.switch_to.frame(parent_iframe)

# iframe element
child_frame=driver.find_element(By.TAG_NAME,"iframe")

# switch to child iframe
driver.switch_to.frame(child_frame)

# locate element
element=driver.find_element(By.TAG_NAME,"p")
print(element.text)

# switch to default content
driver.switch_to.default_content()

# switch to parent frame
driver.switch_to.frame(parent_iframe)

# locate element
parent_element=driver.find_element(By.TAG_NAME,"body")
print(parent_element.text)

# quit browser
driver.quit()