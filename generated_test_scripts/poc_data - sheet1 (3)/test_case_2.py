
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_invalid_login():
    # Set up options for headless, incognito, and disabling pop-ups
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")

    # Launch browser
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Open the page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(5)  # Wait for 5 seconds
        driver.maximize_window()

        # Locate username field and input invalid username
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
        )
        time.sleep(3)
        username_field.send_keys("incorrectUser")

        # Locate password field and input password
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
        )
        time.sleep(3)
        password_field.send_keys("Password123")

        # Locate submit button and click
        submit_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='submit']"))
        )
        time.sleep(3)
        submit_button.click()

        # Verify error message for invalid username
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='error']"))
        )
        time.sleep(3)

        if 'invalid username' in error_message.text.lower():
            print("Test Passed: Correct error message displayed.")
            driver.quit()
            sys.exit(0)
        else:
            print("Test Failed: Incorrect error message displayed.")
            driver.quit()
            sys.exit(1)

    except Exception as e:
        print(f"Test Failed: {e}")
        driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    test_invalid_login()
