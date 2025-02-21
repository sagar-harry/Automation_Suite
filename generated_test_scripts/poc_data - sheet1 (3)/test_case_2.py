
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# Configure Selenium
options = Options()
options.add_argument('--headless')
options.add_argument('--incognito')
options.add_argument('--disable-notifications')
options.add_argument('--disable-popup-blocking')

# Initialize driver
driver = webdriver.Chrome(options=options)

try:
    # Open the page
    driver.get('http://example.com')  # Replace with the actual URL
    time.sleep(5)  # Wait for 5 seconds after opening the page

    # Maximize the page
    driver.maximize_window()

    # Locate username field and enter invalid username
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
    )
    time.sleep(3)  # Wait for 3 seconds before each action
    username_field.send_keys('incorrectUser')

    # Locate password field and enter password
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
    )
    time.sleep(3)  # Wait for 3 seconds before each action
    password_field.send_keys('Password123')

    # Locate and click submit button
    submit_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='submit']"))
    )
    time.sleep(3)  # Wait for 3 seconds before each action
    submit_button.click()

    # Verify error message for invalid username
    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='error']"))
    )
    time.sleep(3)  # Wait for 3 seconds before each action
    assert 'Invalid username' in error_message.text

    # Test case passed
    sys.exit(0)

except Exception as e:
    # Test case failed
    print(str(e))
    sys.exit(1)

finally:
    # Close the driver
    driver.quit()
