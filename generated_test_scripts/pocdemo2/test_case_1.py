
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_login():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-features=NetworkService")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(5)
        driver.maximize_window()

        wait = WebDriverWait(driver, 10)
        
        time.sleep(3)
        username_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
        username_field.send_keys("student")

        time.sleep(3)
        password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
        password_field.send_keys("Password123")

        time.sleep(3)
        submit_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="submit"]')))
        submit_button.click()

        time.sleep(3)
        wait.until(EC.url_contains("success"))

        sys.exit(0)
        
    except Exception as e:
        print(f"Test failed: {str(e)}")
        sys.exit(1)
    
    finally:
        driver.quit()

if __name__ == "__main__":
    test_login()
