import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# open browser
driver=webdriver.Chrome()

# open url
driver.get("https://artoftesting.com/samplesiteforselenium#")
driver.maximize_window()
time.sleep(2)

# locate the link
link=driver.find_elements(By.TAG_NAME,"a")

# print total number of links
print("the total number of links are: ",len(link))

# iterating through loop and printing them one by one
for mylink in link:
    print(mylink.text)