
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def run_test_case():
    try:
        # Configure Selenium options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--incognito")
        
        # Initialize the WebDriver
        driver = webdriver.Chrome(options=chrome_options)
        
        # Open the page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(5)  # Wait for 5 seconds after opening the page
        
        # Maximize the page
        driver.maximize_window()
        
        # Wait and interact with elements
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
        )
        time.sleep(3)
        username_field = driver.find_element(By.XPATH, "//input[@name='username']")
        username_field.send_keys('incorrectUser')

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
        )
        time.sleep(3)
        password_field = driver.find_element(By.XPATH, "//input[@name='password']")
        password_field.send_keys('Password123')

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='submit']"))
        )
        time.sleep(3)
        submit_button = driver.find_element(By.XPATH, "//*[@id='submit']")
        submit_button.click()
        
        # Verify the error message
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='error']"))
        )
        time.sleep(3)
        error_message = driver.find_element(By.XPATH, "//div[@id='error']")
        assert 'your username is invalid!' in error_message.text
        
        driver.quit()
        return 0
    except Exception as e:
        print(f"Test case failed: {e}")
        driver.quit()
        return 1

exit_code = run_test_case()
exit(exit_code)
