
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_ui_scenario():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=NetworkService")
    chrome_options.add_argument("--window-size=1920x1080")

    # Start WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Navigate to the "Test Exceptions" page
        driver.get("URL_OF_TEST_EXCEPTIONS_PAGE")
        time.sleep(5)  # Wait 5 secs after opening the page

        # Wait for 3 seconds before actions
        time.sleep(3)

        # Add a row and enter "burger"
        add_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "XPATH_TO_ADD_BUTTON"))
        )
        add_button.click()
        
        time.sleep(3)  # Wait for 3 seconds each action

        # Enter "burger"
        input_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "XPATH_TO_INPUT_BOX"))
        )
        input_box.send_keys("burger")

        time.sleep(3)  # Wait for 3 seconds each action

        # Click on the "Remove" button
        remove_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='remove_btn']"))
        )
        remove_button.click()

        time.sleep(3)  # Wait for 3 seconds each action

        # Verify the message "Row removed successfully"
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Row 2 was removed')]"))
        )

        assert success_message is not None

        driver.quit()
        sys.exit(0)

    except Exception as e:
        driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    test_ui_scenario()
