
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=NetworkService")

    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the specified URL
    driver.get("https://practicetestautomation.com/practice-test-exceptions/")
    time.sleep(5)
    
    # Maximize the window
    driver.maximize_window()

    # Wait before each action
    time.sleep(3)

    # Wait for the 'Contact' link and click it
    contact_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Contact')]"))
    )
    contact_link.click()

    # Wait for the URL to change and verify it
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://practicetestautomation.com/contact/")
    )

    # Take a screenshot
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")

    # Exit with success
    sys.exit(0)

except Exception as e:
    # Handle any exceptions and exit with failure
    print(f"Test failed: {e}")
    sys.exit(1)

finally:
    # Close the driver
    driver.quit()
