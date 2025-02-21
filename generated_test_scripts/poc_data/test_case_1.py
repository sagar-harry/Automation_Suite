
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-features=NetworkService")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open the page
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(5)  # Waiting for the page to load

    # Maximize the page
    driver.maximize_window()

    # Wait for 3 seconds
    time.sleep(3)

    # Enter the username
    username_field = driver.find_element(By.XPATH, "//input[@name='username']")
    username_field.send_keys("student")

    # Wait for 3 seconds
    time.sleep(3)

    # Enter the password
    password_field = driver.find_element(By.XPATH, "//input[@name='password']")
    password_field.send_keys("Password123")

    # Wait for 3 seconds
    time.sleep(3)

    # Click submit
    submit_button = driver.find_element(By.XPATH, "//*[@id='submit']")
    submit_button.click()

    # Wait for 3 seconds
    time.sleep(3)

    # Verify successful login
    success_message = driver.find_element(By.XPATH, "//h1[text()='Congratulations']")  # Example XPath for success verification
    assert success_message.is_displayed()

    # Exit with code 0
    exit(0)

except Exception as e:
    print(f"Test Failed: {e}")
    # Exit with code 1
    exit(1)

finally:
    # Close the browser
    driver.quit()
