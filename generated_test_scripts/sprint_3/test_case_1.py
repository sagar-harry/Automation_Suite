
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def run_test():
    try:
        # Setting Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-features=NetworkService")

        # Initialize the Chrome WebDriver
        driver = webdriver.Chrome(options=chrome_options)
        
        # Maximizing the browser window
        driver.maximize_window()
        
        # Open the application URL
        driver.get("https://www.saucedemo.com/v1/index.html")
        
        # Wait for 5 seconds
        time.sleep(5)

        # Locate the username field and input the username
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]')))
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")

        # Locate the password field and input the password
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]')))
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")

        # Locate the login button and click to submit
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]')))
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

        # Add assertion or check here if needed

        # Capture a screenshot
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\login_page.png")

        # Exit with success code
        sys.exit(0)

    except Exception as e:
        print(f"Test failed: {e}")
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error_page.png")
        sys.exit(1)

    finally:
        # Close the WebDriver
        driver.quit()

if __name__ == "__main__":
    run_test()
