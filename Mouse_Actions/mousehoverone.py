import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# open browser
driver=webdriver.Chrome()
time.sleep(2)

# open url
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(2)

# teams option locator on cricbuzz.com
teams_locator=driver.find_element(By.ID,"mousehover")

# mouse hover on teams options
act= ActionChains(driver)

act.move_to_element(teams_locator).perform()
time.sleep(3)
print("it worked...!")

