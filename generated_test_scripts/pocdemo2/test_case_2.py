
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time

def test_login_with_invalid_username():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(5)  # Wait for 5 secs after opening the page
        driver.maximize_window()

        # Wait for elements and perform actions
        time.sleep(3)
        username_field = driver.find_element(By.XPATH, "//input[@name='username']")
        
        time.sleep(3)
        password_field = driver.find_element(By.XPATH, "//input[@name='password']")

        time.sleep(3)
        submit_button = driver.find_element(By.XPATH, "//*[@id='submit']")

        username_field.send_keys("incorrectUser")
        time.sleep(3)
        password_field.send_keys("Password123")
        time.sleep(3)
        submit_button.click()

        # Wait for the error message to appear
        time.sleep(3)
        error_message = driver.find_element(By.XPATH, "//div[text()='Your username is invalid!']")

        # Check if error message is displayed
        assert error_message.is_displayed(), "Error message is not displayed"

        # Exit with success status
        exit(0)

    except NoSuchElementException as e:
        print(f"Test Failed: {e}")
        # Exit with failure status
        exit(1)

    finally:
        driver.quit()

test_login_with_invalid_username()
