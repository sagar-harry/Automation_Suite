
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_login_invalid_password():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--disable-features=NetworkService')
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    
    try:
        # Open page
        driver.get('https://practicetestautomation.com/practice-test-login/')
        time.sleep(5)
        
        # Wait and interact with username field
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
        time.sleep(3)
        username_field = driver.find_element(By.XPATH, "//input[@name='username']")
        username_field.send_keys('student')
        
        # Wait and interact with password field
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
        time.sleep(3)
        password_field = driver.find_element(By.XPATH, "//input[@name='password']")
        password_field.send_keys('incorrectPassword')
        
        # Wait and click submit button
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='submit']")))
        time.sleep(3)
        submit_button = driver.find_element(By.XPATH, "//*[@id='submit']")
        submit_button.click()
        
        # Verify error message
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Your password is invalid!']")))
        time.sleep(3)
        error_message = driver.find_element(By.XPATH, "//div[text()='Your password is invalid!']")
        
        assert error_message.is_displayed(), "Error message not displayed"
        
        sys.exit(0) # Test case passed

    except Exception as e:
        print(f"Test case failed: {e}")
        sys.exit(1) # Test case failed

    finally:
        driver.quit()

if __name__ == "__main__":
    test_login_invalid_password()
