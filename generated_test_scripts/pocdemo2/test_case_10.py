
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

try:
    # Set up headless Chrome options
    chrome_options = Options()
    chrome_options.headless = True
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=NetworkService")

    # Start the driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    # Navigate to the URL
    driver.get("https://practicetestautomation.com/practice-test-exceptions/")
    time.sleep(5)

    # Add a new row
    wait = WebDriverWait(driver, 10)
    add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add')]")))
    time.sleep(3)
    add_button.click()

    # Verify "Row 2 was added" message
    confirmation = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='confirmation']")))
    if "Row 2 was added" not in confirmation.text:
        raise AssertionError("Row 2 was not added")

    # Enter "burger" into the newly added row
    new_row_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='row2']/input")))
    time.sleep(3)
    new_row_input.send_keys("burger")

    # Click "Save" button
    save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='save_btn']")))
    time.sleep(3)
    save_button.click()

    # Verify "Row added successfully" message
    confirmation = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='confirmation']")))
    if "Row added successfully" not in confirmation.text:
        raise AssertionError("Row was not added successfully")

    # Click "Remove" button
    remove_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='remove_btn']")))
    time.sleep(3)
    remove_button.click()

    # Verify "Row 2 was removed" message
    confirmation = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='confirmation']")))
    if "Row 2 was removed" not in confirmation.text:
        raise AssertionError("Row 2 was not removed")

    # Successful test case
    sys.exit(0) 

except Exception as e:
    print(f"Test failed with exception: {e}")
    sys.exit(1)

finally:
    driver.quit()
