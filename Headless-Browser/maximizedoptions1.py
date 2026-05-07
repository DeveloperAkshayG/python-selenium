import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options=Options()
options.add_argument("--start-maximized")
options.add_argument("--window-size=1920,1080")

# instantiate driver
driver=webdriver.Chrome(options=options)

# open url
driver.get("https://chinchpoklichachintamani.com/Mar/index.php")
time.sleep(2)

# quit browser
driver.quit()