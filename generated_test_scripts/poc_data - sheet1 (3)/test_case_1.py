
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_login():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")

    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(5)  # Wait for page to load
        driver.maximize_window()

        time.sleep(3)  # Wait before next action
        username_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='username']"))
        )
        username_field.send_keys("student")
        
        time.sleep(3)  # Wait before next action
        password_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='password']"))
        )
        password_field.send_keys("Password123")
        
        time.sleep(3)  # Wait before next action
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='submit']"))
        )
        submit_button.click()
        
        time.sleep(3)  # Wait for result to be visible
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Logged in Successfully')]"))
        )

        assert success_message.is_displayed()
        sys.exit(0)

    except Exception as e:
        print(e)
        sys.exit(1)
    
    finally:
        driver.quit()

test_login()
