
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
import sys

class LoginPage:
    URL = "https://practicetestautomation.com/practice-test-login/"
    USERNAME_LOCATOR = (By.XPATH, "//input[@name='username']")
    PASSWORD_LOCATOR = (By.XPATH, "//input[@name='password']")
    SUBMIT_BUTTON_LOCATOR = (By.XPATH, "//button[@type='submit']")
    LOGOUT_BUTTON_LOCATOR = (By.XPATH, "//a[text()='Log out']")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        time.sleep(5)  # Wait for 5 seconds after page load

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.USERNAME_LOCATOR)
        ).send_keys(username)
        time.sleep(3)  # Wait for 3 seconds before next action

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PASSWORD_LOCATOR)
        ).send_keys(password)
        time.sleep(3)  # Wait for 3 seconds before next action

    def submit(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON_LOCATOR)
        ).click()
        time.sleep(3)  # Wait for 3 seconds after submit

    def verify_successful_login(self):
        assert WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.LOGOUT_BUTTON_LOCATOR)
        ), "Log out button not visible; login failed"

def setup_logger():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    setup_logger()
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=options)
    try:
        driver.maximize_window()
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_username("student")
        login_page.enter_password("Password123")
        login_page.submit()
        login_page.verify_successful_login()
        logging.info("Test passed: Login successful and Log out button is visible.")
        sys.exit(0)
    except AssertionError as e:
        logging.error(f"Test failed: {str(e)}")
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
