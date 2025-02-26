
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-features=NetworkService")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Navigate to the homepage
    driver.get("https://practicetestautomation.com/")
    time.sleep(5)  # Wait for the page to load
    driver.maximize_window()

    # Wait for 3 seconds before the next action
    time.sleep(3)

    # Click on the "Practice" menu
    practice_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Practice')]"))
    )
    practice_menu.click()

    # Wait for the page to load
    time.sleep(3)

    # Verify that the page URL is https://practicetestautomation.com/practice/
    current_url = driver.current_url
    if current_url == "https://practicetestautomation.com/practice/":
        sys.exit(0)  # Exit with code 0 if test case passed
    else:
        sys.exit(1)  # Exit with code 1 if test case failed

except Exception as e:
    print(f"Test failed: {e}")
    sys.exit(1)

finally:
    driver.quit()
