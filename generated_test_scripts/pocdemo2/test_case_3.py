
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

# Setup Chrome options
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--incognito')
options.add_argument('--disable-features=NetworkService')
options.add_argument('--disable-notifications')
options.add_argument('--no-sandbox')

# Initialize webdriver
driver = webdriver.Chrome(options=options)

try:
    # Open the page
    driver.get('https://practicetestautomation.com/practice-test-login/')
    time.sleep(5)  # Wait for 5 seconds after opening the page

    # Maximize the page
    driver.maximize_window()

    # Locate and interact with elements
    username_field = driver.find_element(By.XPATH, "//input[@name='username']")
    password_field = driver.find_element(By.XPATH, "//input[@name='password']")
    submit_button = driver.find_element(By.XPATH, "//*[@id='submit']")

    # Enter the username
    time.sleep(3)
    username_field.send_keys('student')

    # Enter the invalid password
    time.sleep(3)
    password_field.send_keys('incorrectPassword')

    # Click submit
    time.sleep(3)
    submit_button.click()

    # Wait for error message to appear
    time.sleep(3)
    error_message = driver.find_element(By.XPATH, "//div[text()='Your password is invalid!']")

    # Validate error message
    if error_message.is_displayed():
        print("Test case passed!")
        sys.exit(0)
    else:
        print("Error message not displayed as expected.")
        sys.exit(1)

except Exception as e:
    print("An error occurred:", e)
    sys.exit(1)

finally:
    driver.quit()
