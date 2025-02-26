
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
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popups")
chrome_options.add_argument("--disable-features=NetworkService")

# Set up the WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Step 1: Open the page
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.maximize_window()
    time.sleep(5)

    # Step 2: Enter the invalid username
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@name='username']"))
    )
    time.sleep(3)
    username_field.send_keys("incorrectUser")

    # Step 3: Enter the password
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@name='password']"))
    )
    time.sleep(3)
    password_field.send_keys("Password123")

    # Step 4: Click submit
    submit_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='submit']"))
    )
    time.sleep(3)
    submit_button.click()

    # Step 5: Verify error message
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='Your username is invalid!']"))
    )
    time.sleep(3)

    assert "Your username is invalid!" in error_message.text
    sys.exit(0)

except AssertionError:
    sys.exit(1)

finally:
    driver.quit()
