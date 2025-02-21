
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def run_test():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    
    try:
        driver = webdriver.Chrome(options=chrome_options)
    
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(5)
        driver.maximize_window()

        # Enter the username
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='username']"))
        )
        time.sleep(3)
        username_field = driver.find_element(By.XPATH, "//input[@name='username']")
        username_field.send_keys('student')

        # Enter the invalid password
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='password']"))
        )
        time.sleep(3)
        password_field = driver.find_element(By.XPATH, "//input[@name='password']")
        password_field.send_keys('incorrectPassword')

        # Click submit
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='submit']"))
        )
        time.sleep(3)
        submit_button = driver.find_element(By.XPATH, "//*[@id='submit']")
        submit_button.click()

        # Verify error message for invalid password
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@id='error']"))
        )
        time.sleep(3)
        error_message = driver.find_element(By.XPATH, "//div[@id='error']")
        if "Your password is invalid!" in error_message.text:
            print("Test Passed")
            driver.quit()
            sys.exit(0)
        else:
            print("Test Failed")
            driver.quit()
            sys.exit(1)

    except Exception as e:
        print(f"Exception occurred: {e}")
        driver.quit()
        sys.exit(1)

# Run the test case
run_test()
