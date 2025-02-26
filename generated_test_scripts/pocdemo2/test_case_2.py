
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

# Set up the Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-features=NetworkService")

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open the page
    driver.get("https://practicetestautomation.com/practice-test-login/")
    # Maximize the page
    driver.maximize_window()
    # Wait for 3 seconds
    time.sleep(3)

    # Wait for the username field to appear and then enter the invalid username
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
    )
    time.sleep(3)
    username_field.send_keys('incorrectUser')

    # Wait for the password field to appear and then enter the password
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
    )
    time.sleep(3)
    password_field.send_keys('Password123')

    # Wait for the submit button to appear and then click it
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='submit']"))
    )
    time.sleep(3)
    submit_button.click()

    # Wait for the error message to appear and verify it
    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[text()='Your username is invalid!']"))
    )
    time.sleep(3)

    # Test Passed
    sys.exit(0)

except Exception as e:
    # Test Failed
    sys.exit(1)

finally:
    driver.quit()
