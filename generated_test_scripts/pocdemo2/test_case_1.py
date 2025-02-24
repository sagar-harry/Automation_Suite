
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

try:
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=NetworkService")
    chrome_options.add_argument("--disable-notifications")

    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    # Open the page
    driver.maximize_window()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(5)  # Wait for 5 seconds after opening the page

    # Locate username field and enter the username
    wait = WebDriverWait(driver, 10)
    username_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
    time.sleep(3)  # Wait for 3 seconds before action
    username_field.send_keys('student')

    # Locate password field and enter the password
    password_field = driver.find_element(By.XPATH, "//input[@name='password']")
    time.sleep(3)  # Wait for 3 seconds before action
    password_field.send_keys('Password123')

    # Locate and click the submit button
    submit_button = driver.find_element(By.XPATH, "//*[@id='submit']")
    time.sleep(3)  # Wait for 3 seconds before action
    submit_button.click()

    # Verify successful login
    time.sleep(3)  # Wait for 3 seconds before action
    success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Welcome!')]")))
    assert "welcome" in success_message.text.lower()

    # Test case passed
    sys.exit(0)

except Exception as e:
    # Print exception for debugging purposes (optional)
    print(str(e))

    # Test case failed
    sys.exit(1)

finally:
    # Clean up and close the browser
    driver.quit()
