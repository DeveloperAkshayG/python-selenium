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

target_locator=driver.find_element(By.XPATH,"//input[@value='Show']")

act=ActionChains(driver)

#perform right click to open context menu
act.context_click(target_locator).perform()
time.sleep(2)

# close the browser
driver.quit()