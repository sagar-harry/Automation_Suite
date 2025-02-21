
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# Set up options for headless, incognito, and disable features
options = Options()
options.add_argument("--headless")
options.add_argument("--incognito")
options.add_argument("--disable-notifications")
options.add_argument("--disable-features=NetworkService")

# Create the WebDriver instance
driver = webdriver.Chrome(options=options)

try:
    # Open the page
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(5)  # Wait for 5 seconds after opening the page

    # Maximize the page
    driver.maximize_window()

    # Locate the username field and send keys
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@name='username']"))
    )
    username_field = driver.find_element(By.XPATH, "//input[@name='username']")
    time.sleep(3)  # Wait for 3 seconds before action
    username_field.send_keys("incorrectUser")

    # Locate the password field and send keys
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@name='password']"))
    )
    password_field = driver.find_element(By.XPATH, "//input[@name='password']")
    time.sleep(3)  # Wait for 3 seconds before action
    password_field.send_keys("Password123")

    # Locate the submit button and click
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='submit']"))
    )
    submit_button = driver.find_element(By.XPATH, "//*[@id='submit']")
    time.sleep(3)  # Wait for 3 seconds before action
    submit_button.click()

    # Verify the error message
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='error']"))
    )
    error_message = driver.find_element(By.XPATH, "//*[@id='error']").text
    assert error_message == "Your username is invalid!"

    # Exit with code 0 if the test case passed
    sys.exit(0)

except Exception as e:
    print(f"Test failed: {e}")
    # Exit with code 1 if the test case failed
    sys.exit(1)

finally:
    # Close the browser
    driver.quit()
