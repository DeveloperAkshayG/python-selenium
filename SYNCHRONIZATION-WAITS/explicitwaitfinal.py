"""
This script demonstrate explicit wait final
"""
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://artoftesting.com/samplesiteforselenium#")
driver.maximize_window()

# explicit wait
wait=WebDriverWait(driver,20)
alert_btn=wait.until(expected_conditions.visibility_of_element_located((By.ID,"dblClkBtn")))

# create instance of actionchain class
act=ActionChains(driver)

# double click the alert button
act.double_click(alert_btn).perform()
time.sleep(3)

# switch to alert
alert=driver.switch_to.alert

# accept the alert
alert.accept()
time.sleep(3)

# close browser
driver.quit()