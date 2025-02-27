
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

try:
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=NetworkService")

    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    # Maximize the window
    driver.maximize_window()
    
    # Navigate to the homepage
    driver.get("https://practicetestautomation.com/")
    time.sleep(5)  # Wait for 5 seconds

    # Click on the "Home" menu
    time.sleep(3)  # Wait for 3 seconds before action
    home_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Home')]"))
    )
    home_menu.click()

    # Wait for the page to load
    time.sleep(3)  # Wait for 3 seconds

    # Verify that the page URL is https://practicetestautomation.com/
    current_url = driver.current_url
    if current_url == "https://practicetestautomation.com/":
        sys.exit(0)  # Test case passed
    else:
        sys.exit(1)  # Test case failed

except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)  # Test case failed

finally:
    driver.quit()
