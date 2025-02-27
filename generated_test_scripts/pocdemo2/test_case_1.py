
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_login():
    options = Options()
    options.headless = True
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")

    # Open Chrome browser
    driver = webdriver.Chrome(options=options)
    
    try:
        # Open the page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.maximize_window()
        time.sleep(5)
        
        # Wait for elements and perform actions
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys('student')
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys('Password123')
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="submit"]')))
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="submit"]').click()
        
        # Verify successful login
        WebDriverWait(driver, 10).until(EC.url_contains("success"))
        print("Login successful")
        sys.exit(0) # Exit code 0 for success
        
    except Exception as e:
        print(f"Test Failed: {e}")
        sys.exit(1) # Exit code 1 for failure
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_login()
