
import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    try:
        # Configure Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-features=NetworkService")
        
        # Initialize WebDriver
        driver = webdriver.Chrome(options=chrome_options)
        
        # Maximize the window
        driver.maximize_window()
        
        # Navigate to the test page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        
        # Wait for the page to load
        time.sleep(5)
        
        # Locate and click the "Add" button
        add_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add')]"))
        )
        time.sleep(3)
        add_button.click()
        
        # Verify the "Row added successfully" message is displayed
        confirmation = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='confirmation']"))
        )
        assert "Row added successfully" in confirmation.text
        time.sleep(3)
        
        # Enter "burger" into the newly added row input field
        new_row_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='row2']/input"))
        )
        new_row_input.send_keys("burger")
        time.sleep(3)
        
        # Click the "Save" button
        save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='save_btn']"))
        )
        save_button.click()
        time.sleep(3)
        
        # Verify the "Row added successfully" message is displayed again
        confirmation = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='confirmation']"))
        )
        assert "Row added successfully" in confirmation.text
        time.sleep(3)
        
        # Click the "Remove" button for the newly added row
        remove_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='remove_btn']"))
        )
        remove_button.click()
        time.sleep(3)
        
        # Verify the row removal message
        confirmation = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='confirmation']"))
        )
        assert "Row 2 was removed" in confirmation.text

        # Save a screenshot
        os.makedirs('C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots', exist_ok=True)
        driver.save_screenshot('C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png')

    except Exception as e:
        print(f"Test failed: {e}")
        driver.quit()
        sys.exit(1)
    
    # Close the browser
    driver.quit()
    
    sys.exit(0)

if __name__ == "__main__":
    main()
