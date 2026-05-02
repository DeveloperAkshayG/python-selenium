import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://proleed.academy/exercises/selenium/automation-practice-form-with-radio-button-check-boxes-and-drop-down.php")
time.sleep(3)

# write to session storage
driver.execute_script("window.sessionStorage.setItem('chinchpoklicha','chintamani')")
time.sleep(2)

# read value from session storage for key 'chinchpokli'
print('session storage value for key chinchpoklicha : ', driver.execute_script("return window.sessionStorage.getItem('chinchpoklicha')") )

# close browser
driver.quit()