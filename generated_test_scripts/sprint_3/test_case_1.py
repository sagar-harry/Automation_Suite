
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_login():
    try:
        # Setup Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-features=NetworkService")
        
        # Initialize the WebDriver
        driver = webdriver.Chrome(options=chrome_options)
        
        # Open the application page
        driver.get("https://www.saucedemo.com/v1/index.html")
        time.sleep(5)  # Wait for 5 seconds
        driver.maximize_window()

        # Locate elements and perform actions
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='user-name']")))
        time.sleep(3)  # Wait for 3 seconds
        username_input = driver.find_element(By.XPATH, "//*[@id='user-name']")
        username_input.send_keys("standard_user")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='password']")))
        time.sleep(3)  # Wait for 3 seconds
        password_input = driver.find_element(By.XPATH, "//*[@id='password']")
        password_input.send_keys("secret_sauce")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='login-button']")))
        time.sleep(3)  # Wait for 3 seconds
        login_button = driver.find_element(By.XPATH, "//*[@id='login-button']")
        login_button.click()

        # Verify login was successful
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_container")))
        
        # Take a screenshot of the page in the end
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\login_test.png")
        
        # Exit the test successfully
        sys.exit(0)
        
    except Exception as e:
        print(f"An exception occurred: {e}")
        
        # Take a screenshot in case of failure
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\login_test_failed.png")
        
        # Exit with failure code
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    test_login()
