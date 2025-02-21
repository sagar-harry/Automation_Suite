
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import logging
import time
import pytest

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LoginPage:
    URL = "http://example.com/login"
    USERNAME_INPUT = (By.XPATH, "//input[@name='username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE = (By.XPATH, "//*[@id='error-message']")  # adjust this locator to match your app

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        logger.info("Opening the login page")
        self.driver.get(self.URL)
        time.sleep(5)
        self.driver.maximize_window()

    def enter_username(self, username):
        logger.info(f"Entering username: {username}")
        input_field = self.driver.find_element(*self.USERNAME_INPUT)
        time.sleep(3)
        input_field.clear()
        input_field.send_keys(username)

    def enter_password(self, password):
        logger.info("Entering password")
        input_field = self.driver.find_element(*self.PASSWORD_INPUT)
        time.sleep(3)
        input_field.clear()
        input_field.send_keys(password)

    def submit(self):
        logger.info("Clicking submit button")
        button = self.driver.find_element(*self.SUBMIT_BUTTON)
        time.sleep(3)
        button.click()

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text

def test_invalid_login():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-notifications')
    options.add_argument('--incognito')

    driver = webdriver.Chrome(options=options)

    try:
        login_page = LoginPage(driver)
        login_page.open()

        login_page.enter_username('incorrectUser')
        login_page.enter_password('Password123')
        login_page.submit()

        error_message = login_page.get_error_message()
        assert error_message == "Invalid username or password", "Error message not matching"

    except AssertionError as e:
        logger.error("Test failed: %s", e)
        driver.quit()
        exit(1)

    logger.info("Test passed")
    driver.quit()
    exit(0)

if __name__ == '__main__':
    test_invalid_login()
