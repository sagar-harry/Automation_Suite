
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_invalid_login():
    try:
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument('--disable-popup-blocking')
        chrome_options.add_argument('--incognito')
        chrome_options.add_argument('--disable-features=NetworkService')

        # Initialize WebDriver
        driver = webdriver.Chrome(options=chrome_options)

        # Open the login page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.maximize_window()
        time.sleep(5)

        # Locate and interact with elements
        wait = WebDriverWait(driver, 10)

        # Wait for 3 secs before every action
        time.sleep(3)
        username_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
        username_field.send_keys('incorrectUser')

        time.sleep(3)
        password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
        password_field.send_keys('Password123')

        time.sleep(3)
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='submit']")))
        submit_button.click()

        # Verify error message
        time.sleep(3)
        error_message = wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Your username is invalid!']")))
        
        assert error_message.is_displayed()
        
        print("Test Passed")
        driver.quit()
        exit(0)

    except Exception as e:
        print("Test Failed", e)
        driver.quit()
        exit(1)

test_invalid_login()
