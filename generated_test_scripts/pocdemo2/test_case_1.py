
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_login():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-features=NetworkService")
    
    driver = webdriver.Chrome(options=options)

    try:
        driver.maximize_window()
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(5)  # Wait for 5 secs after page load

        # Find username field and enter username
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='username']"))
        )
        time.sleep(3)  # Wait for 3 secs before action
        username_field = driver.find_element(By.XPATH, "//input[@name='username']")
        username_field.send_keys("student")

        # Find password field and enter password
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='password']"))
        )
        time.sleep(3)  # Wait for 3 secs before action
        password_field = driver.find_element(By.XPATH, "//input[@name='password']")
        password_field.send_keys("Password123")

        # Find submit button and click
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='submit']"))
        )
        time.sleep(3)  # Wait for 3 secs before action
        submit_button = driver.find_element(By.XPATH, "//*[@id='submit']")
        submit_button.click()

        # Verify successful login
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "h1"))
        )
        success_message = driver.find_element(By.TAG_NAME, "h1").text
        assert "Logged In Successfully" in success_message

        sys.exit(0)  # Exit with code 0 if test case passed
    except Exception as e:
        print(str(e))
        sys.exit(1)  # Exit with code 1 if test case failed
    finally:
        driver.quit()

test_login()
