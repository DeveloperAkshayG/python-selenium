import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestPositiveScenarios:
    @pytest.mark.login
    def test_positive_login(self):
        # open browser
        driver=webdriver.Chrome()
        time.sleep(2)

        # open url
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.maximize_window()
        time.sleep(2)

        #locating username and entering the same
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")
        time.sleep(2)

        # locating password and entering the password
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")
        time.sleep(2)

        # locating submit button and click on same
        submit_locator = driver.find_element(By.ID, "submit")
        submit_locator.click()
        time.sleep(2)

        # actual url
        actual_url = driver.current_url
        print(actual_url)
        assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

        # verify the page contains logged in successfully
        text_to_match = driver.find_element(By.TAG_NAME, "h1")
        actual_text = text_to_match.text
        print(actual_text)
        assert actual_text == "Logged In Successfully"

        # verify the page contains log out button
        button_expect = driver.find_element(By.LINK_TEXT, "Log out")
        assert button_expect.is_displayed()

