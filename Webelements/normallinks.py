import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# open browser
driver=webdriver.Chrome()
time.sleep(2)

# open url
driver.get("https://www.akasaair.com/flight-booking")
driver.maximize_window()
time.sleep(2)

# locate link and click on it
# link_locator=driver.find_element(By.LINK_TEXT,"Akasa Air")
# link_locator.click()
# time.sleep(2)

# find total number of links and print the number
link_count=driver.find_elements(By.TAG_NAME,'a')
print("total number of links are: ",len(link_count))

# printing the link name
for link in link_count:
    print(link.text)