import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestPositiveScenarios:
    @pytest.mark.login
    @pytest.mark.positive
    def test_checkbox(self):
        driver=webdriver.Chrome()
        time.sleep(2)

        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.maximize_window()
        time.sleep(2)

        checkbox_locator = driver.find_element(By.ID, "checkBoxOption1")
        checkbox_locator.click()
        time.sleep(2)
        checkbox_locator.click()
        time.sleep(2)
        driver.close()

    @pytest.mark.positive
    def test_radio(self):
        driver=webdriver.Chrome()
        time.sleep(2)

        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.maximize_window()
        time.sleep(2)

        radio_locator=driver.find_element(By.XPATH,"//input[@value='radio2']")
        radio_locator.click()
        time.sleep(2)



