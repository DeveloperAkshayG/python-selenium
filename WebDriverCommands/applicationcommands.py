"""
    This script demonstrates application command used in selenium testing
"""


from selenium import webdriver

# open browser
driver=webdriver.Chrome()

# open url
driver.get("https://lalbaugcharaja.com/en/")
driver.maximize_window()

# printing the title of page using title command
print("title is: ",driver.title)

# printing the url of page using current_url command
print("url is: ",driver.current_url)

# printing page source using page_source command
print(driver.page_source)