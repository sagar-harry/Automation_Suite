
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def run_test():
    # Configure browser options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-features=NetworkService")

    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.maximize_window()
        time.sleep(5)

        # Wait for elements and interact
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
        time.sleep(3)
        username_field = driver.find_element(By.XPATH, "//input[@name='username']")
        username_field.send_keys('incorrectUser')

        time.sleep(3)
        password_field = driver.find_element(By.XPATH, "//input[@name='password']")
        password_field.send_keys('Password123')

        time.sleep(3)
        submit_button = driver.find_element(By.XPATH, "//*[@id='submit']")
        submit_button.click()

        # Verify error message
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='error']")))
        time.sleep(3)
        error_message = driver.find_element(By.XPATH, "//*[@id='error']").text
        assert error_message == 'Your username is invalid!'

        # Exit with code 0 if passed
        sys.exit(0)

    except AssertionError:
        # Exit with code 1 if test case failed
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    run_test()
