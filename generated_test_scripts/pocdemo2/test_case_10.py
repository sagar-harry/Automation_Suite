
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

def run_test():
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)

    try:
        # Navigate to the page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        driver.maximize_window()
        time.sleep(5)

        # Wait before actions
        time.sleep(3)

        # Click on the "Add" button to add a new row
        add_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add')]"))
        )
        add_button.click()

        # Verify the message "Row added successfully"
        confirmation_msg = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='confirmation']"))
        )
        if "Row added successfully" not in confirmation_msg.text:
            raise Exception("Row added message not found")

        # Enter "burger" into the newly added row input field
        new_row_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='row2']/input"))
        )
        new_row_input.send_keys("burger")

        # Wait before actions
        time.sleep(3)

        # Click on the "Save" button
        save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='save_btn']"))
        )
        save_button.click()

        # Verify the message "Row added successfully"
        confirmation_msg = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='confirmation']"))
        )
        if "Row added successfully" not in confirmation_msg.text:
            raise Exception("Save row message not found")

        # Wait before actions
        time.sleep(3)

        # Click on the "Remove" button next to the added row
        remove_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='remove_btn']"))
        )
        remove_button.click()

        # Verify the message "Row 2 was removed"
        confirmation_msg = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='confirmation']"))
        )
        if "Row 2 was removed" not in confirmation_msg.text:
            raise Exception("Remove confirmation message not found")

        sys.exit(0)

    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)
    
    finally:
        driver.quit()

if __name__ == "__main__":
    run_test()
