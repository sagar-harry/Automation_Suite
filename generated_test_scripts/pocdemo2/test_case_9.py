
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def run_test_case():
    # Set up Chrome options
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--incognito')
    options.add_argument('--disable-features=NetworkService')
    options.add_argument('--disable-notifications')
    options.add_argument('--start-maximized')

    # Initialize WebDriver
    driver = webdriver.Chrome(options=options)

    try:
        # Navigate to the page
        driver.get('https://practicetestautomation.com/practice-test-exceptions/')
        time.sleep(5)

        # Wait for button and click "Add"
        add_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Add')]"))
        )
        time.sleep(3)
        add_button.click()

        # Verify the add message
        confirmation = WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "confirmation"), "Row 2 was added")
        )
        if not confirmation:
            raise AssertionError("Add confirmation message not found")

        # Enter "burger" in newly added row input field
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='row2']/input"))
        )
        time.sleep(3)
        input_field.send_keys('burger')

        # Click on "Save" button
        save_button = driver.find_element(By.ID, "save_btn")
        time.sleep(3)
        save_button.click()

        # Verify the success message
        success_message = WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "confirmation"), "Row added successfully")
        )
        if not success_message:
            raise AssertionError("Save confirmation message not found")

        sys.exit(0)  # Test passed

    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)  # Test failed

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    run_test_case()
