
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def run_test():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--incognito")
        
        driver = webdriver.Chrome(options=chrome_options)
        
        # Open the page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(5)
        driver.maximize_window()
        
        # Wait for username field and enter username
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
        )
        time.sleep(3)
        username_field = driver.find_element(By.XPATH, "//input[@name='username']")
        username_field.send_keys('student')
        
        # Wait for password field and enter invalid password
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
        )
        time.sleep(3)
        password_field = driver.find_element(By.XPATH, "//input[@name='password']")
        password_field.send_keys('incorrectPassword')
        
        # Wait for submit button and click it
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='submit']"))
        )
        time.sleep(3)
        submit_button = driver.find_element(By.XPATH, "//*[@id='submit']")
        submit_button.click()
        
        # Wait for error message and verify it
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='error']"))
        )
        time.sleep(3)
        error_message = driver.find_element(By.XPATH, "//div[@id='error']")
        assert "invalid" in error_message.text.lower()
        
        driver.quit()
        sys.exit(0)
    except Exception as e:
        print(f"Test failed: {e}")
        driver.quit()
        sys.exit(1)

run_test()
