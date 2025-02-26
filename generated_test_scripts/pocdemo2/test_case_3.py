
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import sys

def test_invalid_login():
    # Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=NetworkService")

    # Create WebDriver instance
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Step 1: Open the page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.maximize_window()
        time.sleep(3)

        # Step 2: Enter the username
        username_field = driver.find_element(By.XPATH, "//input[@name='username']")
        time.sleep(3)
        username_field.send_keys("student")

        # Step 3: Enter the invalid password
        password_field = driver.find_element(By.XPATH, "//input[@name='password']")
        time.sleep(3)
        password_field.send_keys("incorrectPassword")

        # Step 4: Click submit
        submit_button = driver.find_element(By.XPATH, "//*[@id='submit']")
        time.sleep(3)
        submit_button.click()

        # Step 5: Verify error message
        time.sleep(3)
        error_message = driver.find_element(By.XPATH, "//div[text()='Your password is invalid!']")
        
        if error_message.is_displayed():
            print("Test Case Passed.")
            sys.exit(0)
        else:
            print("Test Case Failed: Error message not displayed.")
            sys.exit(1)

    except Exception as e:
        print(f"Test Case Failed due to exception: {e}")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    test_invalid_login()
