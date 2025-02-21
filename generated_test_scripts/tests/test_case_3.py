
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

def run_test():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(5)  # Wait for 5 secs after opening the page
        driver.maximize_window()

        wait = WebDriverWait(driver, 10)

        # Wait for username field and enter username
        username_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
        time.sleep(3)  # Wait for 3 secs before action
        username_field.send_keys("student")

        # Wait for password field and enter password
        password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
        time.sleep(3)
        password_field.send_keys("incorrectPassword")

        # Wait for submit button and click
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='submit']")))
        time.sleep(3)
        submit_button.click()

        # Wait for error message
        error_message = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='error']")))

        # Verification
        assert error_message is not None
        assert "Your password is invalid!" in error_message.text

        driver.quit()
        sys.exit(0)  # Exit with code 0 if test case passed

    except Exception as e:
        driver.quit()
        sys.exit(1)  # Exit with code 1 if test case failed

run_test()
