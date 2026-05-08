import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://chinchpoklichachintamani.com/Mar/index.php")
driver.maximize_window()
time.sleep(5)

# scroll to location(0,800)
driver.execute_script("window.scrollBy(0,800)")
time.sleep(5)
value=driver.execute_script("return window.pageYOffset;")
print("pixel scrolled are -->",value)

# scroll to start
print("scrolling to start")
driver.execute_script("window.scrollBy(0,-800)")
time.sleep(5)
value=driver.execute_script("return window.pageYoffset;")
print("pixel scrolled are --> ",value)

# quit browser
driver.quit()