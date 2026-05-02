import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://demoqa.com/broken")
time.sleep(3)

# write to session storage
driver.execute_script("window.sessionStorage.setItem('hamza','mazaari')")

# read the value from session storage
print(driver.execute_script("return window.sessionStorage.getItem('hamza')"))

# close browser
driver.quit()