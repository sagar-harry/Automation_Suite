
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def run_test():
    # Set Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-features=NetworkService")
    chrome_options.add_argument("--window-size=1920,1080")

    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Navigate to the homepage
        driver.get("https://practicetestautomation.com/")
        time.sleep(5)  # Wait for 5 secs after page opens

        # Maximize the window
        driver.maximize_window()

        # Wait for 3 secs before next action
        time.sleep(3)

        # Click on the "Home" menu
        home_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Home')]"))
        )
        home_menu.click()

        # Wait for page to load
        time.sleep(3)

        # Verify that the page URL is correct
        expected_url = "https://practicetestautomation.com/"
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))

        # Ensure URL is as expected
        if driver.current_url == expected_url:
            print("Test Passed!")
            sys.exit(0)
        else:
            print("Test Failed: URL Mismatch")
            sys.exit(1)
        
    except Exception as e:
        print(f"Test Failed: {str(e)}")
        sys.exit(1)
    
    finally:
        # Quit the driver
        driver.quit()

if __name__ == "__main__":
    run_test()
