"""
    This script demonstrates webdriver application commands used in selenium
"""
import time

from selenium import webdriver

# open browser
driver=webdriver.Chrome()

# open url
driver.get("https://chinchpoklichachintamani.com/Mar/index.php")
driver.maximize_window()
time.sleep(3)

# printing title of page using title command
print("The title is :",driver.title)

#printing the current url of page using current_url command
print("The current url is : ",driver.current_url)

# Getting the page source using page source command
print(driver.page_source)

