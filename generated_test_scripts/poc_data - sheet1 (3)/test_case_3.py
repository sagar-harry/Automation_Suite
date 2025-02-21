
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_invalid_login():
    # Set up options for the Chrome driver
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")

    # Initialize the webdriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Open the login page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(5)  # Wait for 5 secs after opening the page

        # Maximize the window
        driver.maximize_window()

        # Locate the username field and enter the username
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
        time.sleep(3)
        username_field = driver.find_element(By.XPATH, "//input[@name='username']")
        username_field.send_keys("student")

        # Locate the password field and enter the incorrect password
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
        time.sleep(3)
        password_field = driver.find_element(By.XPATH, "//input[@name='password']")
        password_field.send_keys("incorrectPassword")

        # Locate and click the submit button
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='submit']")))
        time.sleep(3)
        submit_button = driver.find_element(By.XPATH, "//*[@id='submit']")
        submit_button.click()

        # Verify the error message for invalid login
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='error']")))
        time.sleep(3)
        error_message = driver.find_element(By.XPATH, "//div[@id='error']").text

        assert error_message == "Your password is invalid!", "Error message does not match the expected text."
        
        # Exit with code 0 if test passed
        sys.exit(0)

    except Exception as e:
        print(f"Test failed: {e}")
        
        # Exit with code 1 if test failed
        sys.exit(1)

    finally:
        # Close the browser
        driver.quit()

# Run the test
test_invalid_login()
