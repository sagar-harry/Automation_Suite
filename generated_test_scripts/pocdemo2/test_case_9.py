
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_ui_scenario():
    try:
        # Configure ChromeOptions
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument('--incognito')
        chrome_options.add_argument('--disable-features=NetworkService')
        
        # Initialize WebDriver
        driver = webdriver.Chrome(options=chrome_options)
        
        # Open the URL
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        time.sleep(5)  # Wait for 5 secs after opening the page
        
        # Maximize the page
        driver.maximize_window()
        time.sleep(3)  # Wait for 3 secs before taking any action
        
        # Locate and click the "Add" button
        add_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Add')]"))
        )
        add_button.click()
        time.sleep(3)  # Wait for 3 secs before taking the next action
        
        # Verify "Row added successfully" message
        confirmation_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='confirmation']"))
        )
        assert confirmation_message.text == "Row added successfully"
        
        # Enter "burger" into the input field of the new row
        input_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='row2']/input"))
        )
        input_field.send_keys("burger")
        time.sleep(3)  # Wait for 3 secs before taking the next action
        
        # Locate and click the "Save" button
        save_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='save_btn']"))
        )
        save_button.click()
        time.sleep(3)  # Wait for 3 secs before taking the next action
        
        # Verify "Row added successfully" message again
        confirmation_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='confirmation']"))
        )
        assert confirmation_message.text == "Row added successfully"
        
        # Close the driver
        driver.quit()
        
        # Exit with success
        sys.exit(0)
        
    except Exception as e:
        # If there is any error, print it and exit with failure
        print(str(e))
        driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    test_ui_scenario()
