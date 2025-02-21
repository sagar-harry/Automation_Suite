
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def run_test():
    # Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Open the page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(5)

        # Maximize the window
        driver.maximize_window()
        time.sleep(3)

        # Enter the username
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
        )
        username_field.send_keys("student")
        time.sleep(3)

        # Enter the invalid password
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
        )
        password_field.send_keys("incorrectPassword")
        time.sleep(3)

        # Click the submit button
        submit_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='submit']"))
        )
        submit_button.click()
        time.sleep(3)

        # Verify error message for invalid password
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='error']"))
        )
        
        assert "Your password is incorrect!" in error_message.text
        sys.exit(0)

    except Exception as e:
        print(f"Test Failed: {e}")
        sys.exit(1)

    finally:
        # Clean up
        driver.quit()

if __name__ == "__main__":
    run_test()
