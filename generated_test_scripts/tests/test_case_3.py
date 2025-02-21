
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_login_with_invalid_password():
    # Configure Chrome options
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)
    try:
        # Open the page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(5)
        driver.maximize_window()

        # Find username field and enter username
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
        )
        time.sleep(3)
        username_field.send_keys("student")

        # Find password field and enter invalid password
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
        )
        time.sleep(3)
        password_field.send_keys("incorrectPassword")

        # Find submit button and click it
        submit_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='submit']"))
        )
        time.sleep(3)
        submit_button.click()

        # Verify error message for invalid password
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='error']"))
        )
        
        # Check if error message is displayed
        time.sleep(3)
        assert "Your username or password is incorrect!" in error_message.text

        # Successful execution
        sys.exit(0)

    except Exception:
        # In case of any failure
        sys.exit(1)

    finally:
        driver.quit()

test_login_with_invalid_password()
