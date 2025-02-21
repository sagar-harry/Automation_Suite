
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
import sys

# Logger setup
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.user_field = (By.XPATH, "//input[@name='username']")
        self.pass_field = (By.XPATH, "//input[@name='password']")
        self.submit_button = (By.XPATH, "//button[@type='submit']")
        self.error_message = (By.XPATH, "//*[contains(text(),'invalid password')]")

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.user_field)).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.pass_field)).send_keys(password)

    def click_submit(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.submit_button)).click()

    def verify_error_message(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.error_message))
            return True
        except:
            return False

def run_test():
    # Chrome options setup
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--incognito')

    # Driver Initialization
    driver = webdriver.Chrome(options=chrome_options)

    try:
        logging.info("Opening the page...")
        driver.get("http://example.com/login")  # Replace with actual URL
        driver.maximize_window()
        time.sleep(5)

        login_page = LoginPage(driver)
        
        logging.info("Entering username...")
        time.sleep(3)
        login_page.enter_username("student")
        
        logging.info("Entering invalid password...")
        time.sleep(3)
        login_page.enter_password("incorrectPassword")
        
        logging.info("Clicking submit...")
        time.sleep(3)
        login_page.click_submit()

        logging.info("Verifying error message...")
        time.sleep(3)
        assert login_page.verify_error_message(), "Error message not found!"
        logging.info("Test case passed.")
        sys.exit(0)

    except Exception as e:
        logging.error("An error occurred: %s", e)
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    run_test()
