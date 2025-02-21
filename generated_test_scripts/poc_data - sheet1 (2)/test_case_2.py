
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_invalid_username():
    try:
        # Setup Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--incognito")

        # Initialize the Chrome driver
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()

        # Open the page
        driver.get('http://example.com')  # Enter your URL here
        time.sleep(5)

        # Wait for the username field and enter invalid username
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
        ).send_keys('incorrectUser')
        time.sleep(3)

        # Wait for the password field and enter password
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
        ).send_keys('Password123')
        time.sleep(3)

        # Wait for the submit button and click it
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        ).click()
        time.sleep(3)

        # Verify the error message for invalid username
        error_message_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='error']"))
        )
        assert 'Invalid username' in error_message_element.text

        # If the test passed
        driver.quit()
        exit(0)

    except Exception:
        # If the test failed
        driver.quit()
        exit(1)

test_invalid_username()
