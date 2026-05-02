import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# OPEN URL
driver.get("https://chinchpoklichachintamani.com/Mar/index.php")
time.sleep(4)

# read cookies
print(driver.get_cookies())

# close browser
driver.quit()