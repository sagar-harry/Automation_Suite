
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_invalid_password():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--incognito')

    driver = webdriver.Chrome(options=options)

    try:
        driver.get('http://example.com')  # replace with actual URL
        time.sleep(5)  # Wait for the page to load completely
        driver.maximize_window()

        # Wait and perform actions
        wait = WebDriverWait(driver, 10)

        # Enter username
        username_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
        time.sleep(3)
        username_field.send_keys('student')

        # Enter invalid password
        password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
        time.sleep(3)
        password_field.send_keys('incorrectPassword')

        # Click submit
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        time.sleep(3)
        submit_button.click()

        # Verify error message for invalid password
        error_message = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='error']")))  # update XPath as needed
        if 'Invalid password' in error_message.text:
            driver.quit()
            exit(0)  # Test case passed
        else:
            driver.quit()
            exit(1)  # Test case failed

    except Exception as e:
        driver.quit()
        exit(1)  # Test case failed due to exception

test_invalid_password()
