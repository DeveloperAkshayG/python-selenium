
from selenium import webdriver

# instantiate driver
driver=webdriver.Chrome()

# open url
driver.get("https://demo.guru99.com/test/login.html#")

# read cookies
print(driver.get_cookies())

print('add new cookies'+ ' \n')

# add cookies
driver.add_cookie(
    {
        'name':'defaultnew',
        'value':'charlie'
    }
)

# read cookies
print(driver.get_cookies())

# close browser
driver.quit()