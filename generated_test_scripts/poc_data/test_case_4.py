
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

def test_homepage():
    try:
        # Setup Chrome options
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--incognito")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-features=NetworkService")

        # Initialize the WebDriver
        driver = webdriver.Chrome(options=options)
        
        # Maximize the browser window
        driver.maximize_window()

        # Step 1: Navigate to the homepage
        driver.get("https://practicetestautomation.com/")
        time.sleep(5)  # Wait for 5 seconds after opening the page

        # Step 2: Click on the "Home" menu
        time.sleep(3)  # Wait for 3 seconds before action
        home_menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Home')]"))
        )
        home_menu.click()

        # Step 3: Wait for the page to load
        time.sleep(3)  # Wait for 3 seconds before action

        # Step 4: Verify the page URL
        current_url = driver.current_url
        if current_url == "https://practicetestautomation.com/":
            print("Test Passed: Correct URL")
            exit_code = 0
        else:
            print("Test Failed: Incorrect URL")
            exit_code = 1

    except Exception as e:
        print(f"Test Failed: An exception occurred - {e}")
        exit_code = 1

    finally:
        # Quit the WebDriver
        driver.quit()

    # Exit with the appropriate code
    sys.exit(exit_code)

if __name__ == "__main__":
    test_homepage()
