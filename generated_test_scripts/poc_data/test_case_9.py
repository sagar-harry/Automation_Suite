
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome options
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-notifications')
options.add_argument('--incognito')
options.add_argument('--disable-features=NetworkService')

try:
    # Initialize the WebDriver
    driver = webdriver.Chrome(options=options)
    
    # Maximize the page
    driver.maximize_window()
    
    # Navigate to the page
    driver.get('https://example.com/test-exceptions')
    time.sleep(5)  # Wait for 5 seconds after opening the page

    # Find the "Add" button and click it
    add_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Add')]"))
    )
    time.sleep(3)  # Wait for 3 seconds before the action
    add_button.click()

    # Verify the message "Row added successfully"
    confirmation_msg = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, "//*[@id='confirmation']"), "Row added successfully")
    )
    assert confirmation_msg == True

    # Enter "burger" into the newly added row input field
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='row2']/input"))
    )
    time.sleep(3)  # Wait for 3 seconds before the action
    input_field.send_keys("burger")

    # Click on the "Save" button
    save_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='save_btn']"))
    )
    time.sleep(3)  # Wait for 3 seconds before the action
    save_button.click()

    # Verify the message "Row added successfully"
    confirmation_msg = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, "//*[@id='confirmation']"), "Row added successfully")
    )
    assert confirmation_msg == True

    # Exit with exit code 0 if test case passed
    driver.quit()
    exit(0)
    
except Exception as e:
    print(f"Test failed: {e}")
    # Exit with exit code 1 if test case failed
    driver.quit()
    exit(1)
