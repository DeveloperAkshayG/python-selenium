
from selenium import webdriver
from selenium.webdriver.common.by import By

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://the-internet.herokuapp.com/iframe")

# iframe element
iframe_element=driver.find_element(By.XPATH,"//iframe[@title='Rich Text Area']")

# switch to iframe
driver.switch_to.frame(iframe_element)

# find element of interest
element_of_interest=driver.find_element(By.ID,"tinymce")
print(element_of_interest.text)
print(element_of_interest.tag_name)

# switch to main content
driver.switch_to.default_content()
outside_element=driver.find_element(By.LINK_TEXT,"Elemental Selenium")
print(outside_element.tag_name)

# quit browser
driver.quit()