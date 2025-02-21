
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuring Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--disable-features=NetworkService')

exit_code = 1  # Default to failure

try:
    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    
    # Open the page
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(5)

    # Username field
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
    )
    time.sleep(3)
    username_field.send_keys('incorrectUser')

    # Password field
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
    )
    time.sleep(3)
    password_field.send_keys('Password123')

    # Submit button
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='submit']"))
    )
    time.sleep(3)
    submit_button.click()

    # Error Message
    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='error']"))
    )
    time.sleep(3)
    
    # Verify error message text
    assert 'your username is invalid!' in error_message.text.lower(), "Error message does not match"

    exit_code = 0  # Test case passed

except Exception as e:
    print(f"Test failed: {e}")

finally:
    driver.quit()
    exit(exit_code)
