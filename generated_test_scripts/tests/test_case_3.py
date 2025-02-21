
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-features=NetworkService")
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

def test_login_failure():
    try:
        # Open the page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(5)

        # Wait and enter username
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
        time.sleep(3)
        username_field = driver.find_element(By.XPATH, "//input[@name='username']")
        username_field.send_keys("student")

        # Wait and enter password
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
        time.sleep(3)
        password_field = driver.find_element(By.XPATH, "//input[@name='password']")
        password_field.send_keys("incorrectPassword")

        # Wait and click submit
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='submit']")))
        time.sleep(3)
        submit_button = driver.find_element(By.XPATH, "//*[@id='submit']")
        submit_button.click()

        # Verify error message
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='error']")))
        time.sleep(3)
        error_message = driver.find_element(By.XPATH, "//div[@id='error']")
        
        if "incorrect" in error_message.text.lower():
            print("Test Passed")
            sys.exit(0)
        else:
            print("Test Failed")
            sys.exit(1)
    except Exception as e:
        print(f"Test Failed: {e}")
        sys.exit(1)
    finally:
        driver.quit()

test_login_failure()
