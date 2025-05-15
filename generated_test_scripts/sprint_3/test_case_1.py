
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def test_login():
    try:
        # Set Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-features=NetworkService")
        
        # Initialize the Chrome driver
        driver = webdriver.Chrome(options=chrome_options)
        
        # Maximize the window
        driver.maximize_window()
        
        # Open the application URL
        driver.get("https://www.saucedemo.com/v1/index.html")
        
        # Wait after opening the URL
        time.sleep(5)

        # Define locators
        username_locator = (By.XPATH, '//*[@id="user-name"]')
        password_locator = (By.XPATH, '//*[@id="password"]')
        login_button_locator = (By.XPATH, '//*[@id="login-button"]')

        # Wait for elements to appear
        wait = WebDriverWait(driver, 10)
        
        # Wait and enter username
        wait.until(EC.visibility_of_element_located(username_locator))
        time.sleep(3)
        driver.find_element(*username_locator).send_keys("standard_user")

        # Wait and enter password
        wait.until(EC.visibility_of_element_located(password_locator))
        time.sleep(3)
        driver.find_element(*password_locator).send_keys("secret_sauce")
        
        # Wait and click login
        wait.until(EC.element_to_be_clickable(login_button_locator))
        time.sleep(3)
        driver.find_element(*login_button_locator).click()

        # Verify login was successful and you're on the next page (example check)
        wait.until(EC.url_changes("https://www.saucedemo.com/v1/index.html"))

        # Save a screenshot
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\post_login.png")
        
        # Exit with success code
        sys.exit(0)

    except Exception as e:
        # Print exception details for debugging
        print(str(e))

        # Save a screenshot
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error.png")
        
        # Exit with failure code
        sys.exit(1)

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    test_login()
