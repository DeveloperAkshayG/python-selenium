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

# locate the target element
target_locator=driver.find_element(By.ID,"mousehover")
driver.execute_script("arguments[0].scrollIntoView();",target_locator)
value=driver.execute_script("return window.pageYOffset")
print("the pixels scrolled are:",value)
time.sleep(3)

# create object of class actionchains
act=ActionChains(driver)

# perform mouse hover operation
act.move_to_element(target_locator).perform()
time.sleep(3)

# close the browser
driver.quit()

