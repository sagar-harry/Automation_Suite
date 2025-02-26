
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import sys

try:
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-features=NetworkService")

    # Initialize the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the practice test page
    driver.maximize_window()
    driver.get("https://practicetestautomation.com/practice-test-exceptions/")
    time.sleep(5)  # Wait for 5 seconds after opening the page

    time.sleep(3)  # Wait for 3 seconds before any action

    # Click on the "Contact" menu
    contact_menu = driver.find_element(By.XPATH, "//a[contains(text(),'Contact')]")
    contact_menu.click()

    time.sleep(3)  # Wait for 3 seconds for the page to load

    # Verify that the page URL is as expected
    time.sleep(3)  # Wait for the elements to appear
    if driver.current_url == "https://practicetestautomation.com/contact/":
        sys.exit(0)  # Exit with code 0 if test case passed
    else:
        sys.exit(1)  # Exit with code 1 if test case failed

finally:
    driver.quit()
