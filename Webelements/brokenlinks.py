import time

import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By

# open browser
driver=webdriver.Chrome()

# open url
driver.get("https://artoftesting.com/samplesiteforselenium#")
driver.maximize_window()
time.sleep(2)

# locate all the links
link=driver.find_elements(By.TAG_NAME,"a")

# count variable for calculating broken link
count=0

# iterating through links to check broken link
for mylink in link:
    url=mylink.get_attribute('href')
    try:
        res=requests.head(url)
        if res.status_code >=400:
            print(url,"  is a broken link")
            count +=1
        else:
            print(url,"  is a valid link")
    except:
        print(url," link could not be checked for broken link or not")
        count+=1

print("the total number of broken link are: ",count)
