
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

try:
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=NetworkService")
    
    # Initialize a Chrome browser instance
    driver = webdriver.Chrome(options=chrome_options)

    # Maximize the page
    driver.maximize_window()

    # Navigate to the URL
    driver.get("https://practicetestautomation.com/practice-test-exceptions/")
    
    # Wait for 5 seconds
    time.sleep(5)

    # Wait for 3 secs before clicking
    time.sleep(3)

    # Click on the "Contact" menu
    contact_menu = driver.find_element(By.XPATH, "//a[contains(text(),'Contact')]")
    contact_menu.click()

    # Wait for 3 secs before checking URL
    time.sleep(3)
    
    # Validate the page URL
    expected_url = "https://practicetestautomation.com/contact/"
    actual_url = driver.current_url

    if actual_url == expected_url:
        sys.exit(0)  # Test case passed
    else:
        sys.exit(1)  # Test case failed

except Exception as e:
    sys.exit(1)

finally:
    # Close the browser
    driver.quit()
