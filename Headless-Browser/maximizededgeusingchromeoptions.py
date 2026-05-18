"""
This script demonstrates maximized edge at the time browser is launched using chromeoptions
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

edge_option = webdriver.EdgeOptions()
edge_option.add_argument("--start-maximized")

# instantiate driver
driver = webdriver.Edge(options=edge_option)

# open url
driver.get("https://rahulshettyacademy.com/AutomationPractice/#")
time.sleep(3)

# drop down locator
drop_down = driver.find_element(By.ID, "dropdown-class-example")

# CREATE INSTANCE OF SELECT CLASS
mydrop = Select(drop_down)

# select by visible text
mydrop.select_by_visible_text("Option3")
print("option 3 selected...")
time.sleep(2)
mydrop.select_by_visible_text("Option1")
time.sleep(2)
print("option 1 selected....")
mydrop.select_by_visible_text("Option2")
time.sleep(2)
print("option 2 selected....")

# quit browser
driver.quit()
