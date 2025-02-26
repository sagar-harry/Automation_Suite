
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import sys

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-features=NetworkService")

# Initialize the Chrome driver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Navigate to the homepage
    driver.get("https://practicetestautomation.com/")
    time.sleep(3)  # Wait for 3 seconds after opening the page

    # Maximize the browser window
    driver.maximize_window()
    time.sleep(3)  # Wait for 3 seconds

    # Click the "Courses" menu
    courses_menu = driver.find_element(By.XPATH, "//a[contains(text(),'Courses')]")
    courses_menu.click()
    time.sleep(3)  # Wait for 3 seconds

    # Wait for the page to load and verify the URL
    if driver.current_url == "https://practicetestautomation.com/courses/":
        sys.exit(0)  # Test case passed
    else:
        sys.exit(1)  # Test case failed

except Exception as e:
    print(str(e))
    sys.exit(1)  # Test case failed

finally:
    # Close the browser
    driver.quit()
