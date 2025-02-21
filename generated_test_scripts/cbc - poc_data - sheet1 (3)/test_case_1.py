
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920,1080")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open the page
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(5)  # Wait for 5 seconds after opening the page

    # Maximize window (if not headless, for headless this size is set in options)
    driver.maximize_window()

    # Enter the username
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@name='username']"))
    ).send_keys("student")
    time.sleep(3)  # Wait for 3 seconds before next action

    # Enter the password
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@name='password']"))
    ).send_keys("Password123")
    time.sleep(3)  # Wait for 3 seconds before next action

    # Click submit
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='submit']"))
    ).click()
    time.sleep(3)  # Wait for 3 seconds before next action

    # Verify the message
    message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='loop-container']/div/article/div[1]/h1"))
    ).text

    if message == 'Logged In Successfully':
        exit_code = 0
    else:
        exit_code = 1

except Exception as e:
    exit_code = 1
    print(f"Test Failed: {str(e)}")

finally:
    driver.quit()
    sys.exit(exit_code)
