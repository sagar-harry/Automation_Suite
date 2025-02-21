
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import sys

# Setup Chrome options
options = Options()
options.headless = True
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_argument("--incognito")

# Initialize the Chrome driver
driver = webdriver.Chrome(options=options)

try:
    # Open the URL
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(5)  # Wait for 5 secs
    driver.maximize_window()

    # Wait for 3 secs before the next action
    time.sleep(3)
    
    # Find and enter username
    username_field = driver.find_element(By.XPATH, "//input[@name='username']")
    username_field.send_keys("student")
    
    # Wait for 3 secs before the next action
    time.sleep(3)
    
    # Find and enter password
    password_field = driver.find_element(By.XPATH, "//input[@name='password']")
    password_field.send_keys("Password123")
    
    # Wait for 3 secs before the next action
    time.sleep(3)
    
    # Find and click submit
    submit_button = driver.find_element(By.XPATH, "//*[@id='submit']")
    submit_button.click()
    
    # Wait for 3 secs before the next action
    time.sleep(3)
    
    # Verify successful login
    success_message = driver.find_element(By.TAG_NAME, "body").text
    assert "Logged In Successfully" in success_message

    # Exit with success code
    sys.exit(0)
except Exception as e:
    # Print the error and exit with failed code
    print(f"Test failed: {e}")
    sys.exit(1)
finally:
    driver.quit()
