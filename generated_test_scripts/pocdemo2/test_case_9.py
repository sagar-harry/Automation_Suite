
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import sys

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-features=NetworkService")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Navigate to the page
    driver.get("https://practicetestautomation.com/practice-test-exceptions/")
    driver.maximize_window()
    time.sleep(5)  # Wait for 5 seconds after opening the page

    # Click on the "Add" button
    add_button = driver.find_element(By.XPATH, "//button[contains(text(),'Add')]")
    add_button.click()
    time.sleep(3)  # Wait for 3 seconds

    # Verify "Row added successfully" message
    confirmation_msg = driver.find_element(By.XPATH, "//*[@id='confirmation']")
    if "Row added successfully" not in confirmation_msg.text:
        sys.exit(1)

    # Enter "burger" into the newly added row input field
    input_field = driver.find_element(By.XPATH, "//*[@id='row2']/input")
    input_field.send_keys("burger")
    time.sleep(3)  # Wait for 3 seconds

    # Click on the "Save" button
    save_button = driver.find_element(By.XPATH, "//*[@id='save_btn']")
    save_button.click()
    time.sleep(3)  # Wait for 3 seconds

    # Verify "Row added successfully" message after saving
    confirmation_msg = driver.find_element(By.XPATH, "//*[@id='confirmation']")
    if "Row added successfully" not in confirmation_msg.text:
        sys.exit(1)

    sys.exit(0)

except Exception as e:
    print(str(e))
    sys.exit(1)

finally:
    driver.quit()
