
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-features=NetworkService")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open the webpage
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(5)
    driver.maximize_window()

    # Wait for the Username field and enter invalid username
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//input[@name="username"]'))
    )
    time.sleep(3)
    username_field = driver.find_element(By.XPATH, '//input[@name="username"]')
    username_field.send_keys('incorrectUser')

    # Wait for the Password field and enter password
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//input[@name="password"]'))
    )
    time.sleep(3)
    password_field = driver.find_element(By.XPATH, '//input[@name="password"]')
    password_field.send_keys('Password123')

    # Wait for the Submit button and click it
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="submit"]'))
    )
    time.sleep(3)
    submit_button = driver.find_element(By.XPATH, '//*[@id="submit"]')
    submit_button.click()

    # Wait for the Error Message and verify it
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//div[text()="Your username is invalid!"]'))
    )
    error_message = driver.find_element(By.XPATH, '//div[text()="Your username is invalid!"]')
    assert error_message.is_displayed(), "Test case failed: Error message is not displayed."

    # Exit with a success code if the error message is displayed
    sys.exit(0)

except Exception as e:
    print(f"Exception occurred: {e}")

finally:
    # Exit with a failure code if an exception was raised
    sys.exit(1)
    driver.quit()
