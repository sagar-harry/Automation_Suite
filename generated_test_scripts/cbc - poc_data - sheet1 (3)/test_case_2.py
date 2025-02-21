
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_invalid_login():
    # Set up options for Selenium WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    
    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # Open the page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(5)
        driver.maximize_window()

        # Wait for 3 secs before every action
        time.sleep(3)

        # Find the username input field and enter the username
        username_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='username']"))
        )
        username_field.send_keys('incorrectUser')

        # Wait for 3 secs
        time.sleep(3)

        # Find the password input field and enter the password
        password_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='password']"))
        )
        password_field.send_keys('Password123')

        # Wait for 3 secs
        time.sleep(3)

        # Find the submit button and click
        submit_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='submit']"))
        )
        submit_button.click()

        # Wait for 3 secs
        time.sleep(3)

        # Verify the error message
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='error']"))
        )
        assert error_message.text == "Your username is invalid!"

        # Exit with exit code 0 if test case passed
        print("Test Passed")
        sys.exit(0)

    except Exception as e:
        print(f"Test Failed: {e}")
        sys.exit(1)

    finally:
        driver.quit()

test_invalid_login()
