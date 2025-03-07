
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys
from compare_sentences import compare_sentences

# Set up browser options
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")

# Initialize the WebDriver
driver = webdriver.Chrome(options=options)

try:
    # Maximize the window
    driver.maximize_window()
    
    # Navigate to the home page
    driver.get("https://saucedemo.com")
    
    # Wait for 3 seconds before the next action
    time.sleep(3)
    
    # Locate and click the login button without entering credentials
    login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
    time.sleep(3)  # Wait before clicking
    login_button.click()
    
    # Wait for 3 seconds before checking for error message
    time.sleep(3)
    
    # Locate the error message element and assert its text
    expected_error_message = "Epic sadface: Username is required"
    error_message_element = driver.find_element(By.XPATH, "//div[@class='error-message-container']")
    actual_error_message = error_message_element.text
    
    # Use compare_sentences to assert error message
    if compare_sentences(expected_error_message, actual_error_message):
        print("Test passed: Correct error message displayed.")
        sys.exit(0)
    else:
        print("Test failed: Incorrect error message displayed.")
        sys.exit(1)

except Exception as e:
    print(f"Test failed with exception: {e}")
    sys.exit(1)

finally:
    # Close the browser
    driver.quit()
