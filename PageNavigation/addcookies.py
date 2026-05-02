import time

from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# OPEN URL
driver.get("https://chinchpoklichachintamani.com/Mar/")
time.sleep(4)

# add cookies
driver.add_cookie(
    {
        'name':'chintamani',
        'value':'mumbaicha raja'
    }
)


time.sleep(2)

# read cookies
print(driver.get_cookies())

# close browser
driver.quit()