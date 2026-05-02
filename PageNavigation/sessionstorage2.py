import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://www.cricbuzz.com")
time.sleep(5)

# write to session storage
driver.execute_script("window.sessionStorage.setItem('India','Kohli')")

# read value from session storage
print('the session value for India is: ',driver.execute_script("return window.sessionStorage.getItem('India')"))

# close browser
driver.quit()