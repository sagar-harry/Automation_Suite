
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

def test_invalid_login():
    try:
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-features=NetworkService")

        # Initialize webdriver
        driver = webdriver.Chrome(options=chrome_options)

        # Open the web page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(5)
        
        # Maximize the page
        driver.maximize_window()

        # Wait for username field visibility and act
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys('student')
        time.sleep(3)

        # Wait for password field visibility and act
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys('incorrectPassword')
        time.sleep(3)

        # Wait for submit button visibility and act
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='submit']")))
        driver.find_element(By.XPATH, "//*[@id='submit']").click()
        time.sleep(3)

        # Verify error message for invalid password
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='error']")))
        error_message = driver.find_element(By.XPATH, "//div[@id='error']").text
        assert "Your password is invalid!" in error_message

        # Exit with success code
        driver.quit()
        sys.exit(0)

    except Exception as e:
        print(f"Test failed: {e}")
        driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    test_invalid_login()
