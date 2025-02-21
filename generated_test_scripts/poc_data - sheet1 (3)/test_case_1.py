
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

def test_login():
    # Options for running Chrome in headless mode, incognito, and without notifications
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    
    try:
        # Setup WebDriver
        driver = webdriver.Chrome(options=chrome_options)
        
        # Open the test page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(5)  # Wait for 5 secs after opening the page
        driver.maximize_window()
        
        # Locate and interact with the username field
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='username']"))
        ).send_keys("student")
        time.sleep(3)  # Wait for 3 secs before next action
        
        # Locate and interact with the password field
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='password']"))
        ).send_keys("Password123")
        time.sleep(3)  # Wait for 3 secs before next action
        
        # Locate and click the submit button
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='submit']"))
        ).click()
        time.sleep(3)  # Wait for 3 secs before next action
        
        # Verify if the login was successful
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[text()='Logged in Successfully']"))
        )
        if success_message.is_displayed():
            sys.exit(0)  # Test passed
        else:
            sys.exit(1)  # Test failed
            
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)  # Test failed

    finally:
        # Close the driver
        driver.quit()

# Run the test
if __name__ == "__main__":
    test_login()
