
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

try:
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    driver.get("https://practicetestautomation.com/practice-test-exceptions/")
    time.sleep(5)

    wait = WebDriverWait(driver, 10)

    # Wait for Add button and click
    add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add')]")))
    time.sleep(3)
    add_button.click()

    # Wait for confirmation message
    confirmation_msg = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='confirmation']")))
    assert "Row added successfully" in confirmation_msg.text, "Add operation failed"

    # Input 'burger' into the new row
    input_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='row2']/input")))
    time.sleep(3)
    input_field.send_keys("burger")

    # Wait for Save button and click
    save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='save_btn']")))
    time.sleep(3)
    save_button.click()

    # Verify message after save
    confirmation_msg = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='confirmation']")))
    time.sleep(3)
    assert "Row added successfully" in confirmation_msg.text, "Save operation failed"

    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
    driver.quit()
    sys.exit(0)

except (AssertionError, TimeoutException, WebDriverException) as e:
    print(f"An error occurred: {e}")
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot_failed.png")
    driver.quit()
    sys.exit(1)
