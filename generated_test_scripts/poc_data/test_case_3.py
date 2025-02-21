
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def main():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-notifications')
    options.add_argument('--incognito')
    options.add_argument('--disable-features=NetworkService')

    driver = webdriver.Chrome(options=options)

    try:
        # Step 1: Open the page
        driver.get('https://practicetestautomation.com/practice-test-login/')
        time.sleep(5)  # Wait for 5 secs after opening the page
        driver.maximize_window()

        # Step 2: Enter the username
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
        )
        time.sleep(3)
        username_field = driver.find_element(By.XPATH, "//input[@name='username']")
        username_field.send_keys('student')

        # Step 3: Enter the invalid password
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
        )
        time.sleep(3)
        password_field = driver.find_element(By.XPATH, "//input[@name='password']")
        password_field.send_keys('incorrectPassword')

        # Step 4: Click submit
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='submit']"))
        )
        time.sleep(3)
        submit_button = driver.find_element(By.XPATH, "//*[@id='submit']")
        submit_button.click()

        # Step 5: Verify error message
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='Your password is invalid!']"))
        )
        time.sleep(3)
        error_message = driver.find_element(By.XPATH, "//div[text()='Your password is invalid!']")
        assert error_message.is_displayed(), "Error message not displayed"
        
        print("Test passed")
        sys.exit(0)

    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
