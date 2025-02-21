
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def test_login():
    try:
        # Setup Chrome options
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument('--disable-popup-blocking')
        chrome_options.add_argument('--incognito')

        # Initialize webdriver
        driver = webdriver.Chrome(options=chrome_options)

        # Open the page
        driver.get('https://practicetestautomation.com/practice-test-login/')
        time.sleep(5)
        driver.maximize_window()

        # Enter username
        time.sleep(3)
        username_field = driver.find_element(By.XPATH, "//input[@name='username']")
        username_field.send_keys('student')

        # Enter password
        time.sleep(3)
        password_field = driver.find_element(By.XPATH, "//input[@name='password']")
        password_field.send_keys('Password123')

        # Click submit
        time.sleep(3)
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()

        # Verify successful login
        time.sleep(3)
        # Assuming success message display or redirection logic here
        logout_visible = driver.find_element(By.XPATH, "//*[text()='Log out']").is_displayed()
        
        # Exit with the appropriate code
        if logout_visible:
            exit_code = 0
        else:
            exit_code = 1

    except Exception as e:
        exit_code = 1
        print(f"Test failed: {e}")

    finally:
        # Close the browser
        driver.quit()
        exit(exit_code)

test_login()
