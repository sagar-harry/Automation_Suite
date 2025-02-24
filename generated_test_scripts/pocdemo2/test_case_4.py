
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def run_test():
    # Setting up Chrome options for headless, incognito mode and disabling notifications
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-features=NetworkService")
    chrome_options.add_argument("--window-size=1920x1080")

    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Navigate to the homepage
        driver.get("https://practicetestautomation.com/")
        time.sleep(5)  # Wait for 5 seconds after opening the page
        driver.maximize_window()
        
        # Click the "Home" menu
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Home')]")))
        time.sleep(3)  # Wait for 3 seconds before action
        home_menu = driver.find_element(By.XPATH, "//a[contains(text(),'Home')]")
        home_menu.click()

        # Wait for the page to load
        WebDriverWait(driver, 10).until(EC.url_to_be("https://practicetestautomation.com/"))
        time.sleep(3)  # Wait for 3 seconds before verifying

        # Verify if the URL is correct
        current_url = driver.current_url
        if current_url == "https://practicetestautomation.com/":
            sys.exit(0)  # Test passed

    except Exception as e:
        # If any exception occurs
        print(f"Test failed due to {e}")
        sys.exit(1)  # Test failed

    finally:
        # Always close the driver
        driver.quit()

if __name__ == "__main__":
    run_test()
