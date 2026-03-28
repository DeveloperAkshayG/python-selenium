import time

import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By

# open browser
driver=webdriver.Chrome()
time.sleep(2)

# open url
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()
time.sleep(2)

# locate all link
alllinks=driver.find_elements(By.TAG_NAME,"a")
count=0

# using for loop iterate through link and verify link is broken
for link in alllinks:
    url=link.get_attribute('href')
    try:
        res=requests.head(url)
    except:
        None
    if res.status_code >=400:
        print(url,' is a broken link')
        count+=1
    else:
        print(url,' is a valid link')

# print total number of broken link
print("the total broken links are: ",count)