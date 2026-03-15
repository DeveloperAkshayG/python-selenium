import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestNegativescenarios:
    @pytest.mark.negative
    def test_negative_scenario_one(self):
        driver = webdriver.Chrome()
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.maximize_window()
        time.sleep(1)
        username_locator=driver.find_element(By.ID,"username")
        username_locator.send_keys("incorrectUser")
        time.sleep(1)
        password_locator=driver.find_element(By.ID,"password")
        password_locator.send_keys("Password123")
        time.sleep(1)
        login_locator=driver.find_element(By.ID,"submit")
        login_locator.click()
        time.sleep(1)

        # verify error message is displayed
        error_message_locator=driver.find_element(By.ID,"error")
        assert error_message_locator.is_displayed()

        # verify error message text is Your username is invalid!
        error_text=error_message_locator.text
        assert error_text == "Your username is invalid!"

    @pytest.mark.negative
    def test_negative_scenario_second(self):
        driver = webdriver.Chrome()
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.maximize_window()
        time.sleep(1)
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")
        time.sleep(1)
        password_locator = driver.find_element(By.ID, "password")
        password_locator.send_keys("incorrectPassword")
        time.sleep(1)
        login_locator = driver.find_element(By.ID, "submit")
        login_locator.click()
        time.sleep(1)

        # verify error message is displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed()

        # verify the error message using assert
        error_text = error_message_locator.text
        assert error_text == "Your password is invalid!"

