
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_scenario():
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=NetworkService")

    # Initialize the driver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Maximize window and disable pop-up blocking
        driver.maximize_window()

        # Navigate to the specified URL
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        
        # Wait for the page to load
        time.sleep(5)

        # Wait for 3 seconds before each action
        time.sleep(3)

        # Click the "Add" button
        add_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add')]"))
        )
        add_button.click()

        # Wait for 3 seconds
        time.sleep(3)

        # Verify if "Row added successfully" message appears
        confirmation_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='confirmation']"))
        )
        if confirmation_message.text != "Row added successfully":
            sys.exit(1)

        # Input "burger" in the new row
        new_row_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='row2']/input"))
        )
        new_row_input.send_keys("burger")

        # Wait for 3 seconds
        time.sleep(3)

        # Click the "Save" button
        save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='save_btn']"))
        )
        save_button.click()

        # Wait for 3 seconds
        time.sleep(3)

        # Verify if save confirmation message appears
        final_confirmation_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='confirmation']"))
        )
        if final_confirmation_message.text != "Row added successfully":
            sys.exit(1)

        sys.exit(0)

    except Exception as e:
        print(e)
        sys.exit(1)

    finally:
        # Close the driver
        driver.quit()

test_scenario()
