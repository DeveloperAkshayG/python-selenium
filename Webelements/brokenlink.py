import time

import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By

# open browsers
driver=webdriver.Chrome()
time.sleep(2)

# open url
driver.get("https://proleed.academy/exercises/selenium/automation-practice-form-with-radio-button-check-boxes-and-drop-down.php")
driver.maximize_window()
time.sleep(2)

# locate all the link
alllinks=driver.find_elements(By.TAG_NAME,"a")

# variable to count broken link
count=0

# iterating through links to find broken link and print broken link
for links in alllinks:
    url=links.get_attribute('href')
    try:
        res = requests.head(url)
        if res.status_code >= 400:
            print(url,"  is broken link")
            count += 1
        else:
            print(url, "  is valid link")

    except:
        print(url ,'  could not be checked as broken ')
        count += 1

# printing total number of broken link
print("the total number of broken links are: ",count)
