
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

def test_login():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-notifications')
    options.add_argument('--incognito')
    options.add_argument('--disable-features=NetworkService')

    driver = webdriver.Chrome(options=options)

    try:
        driver.get('https://practicetestautomation.com/practice-test-login/')
        time.sleep(5)
        driver.maximize_window()
        
        time.sleep(3)
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
        )
        username_field.send_keys('student')

        time.sleep(3)
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
        )
        password_field.send_keys('Password123')

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='submit']"))
        )
        submit_button.click()

        time.sleep(3)
        # Verify successful login
        WebDriverWait(driver, 10).until(
            EC.url_contains("success")
        )
        
        print("Test Passed")
        sys.exit(0)

    except Exception as e:
        print(f"Test Failed: {e}")
        sys.exit(1)

    finally:
        driver.quit()
        
test_login()
