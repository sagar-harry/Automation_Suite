
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

# Set Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-features=NetworkService")

# Initialize driver
driver = webdriver.Chrome(options=options)

try:
    # Navigate to the practice test page
    driver.get("https://practicetestautomation.com/practice-test-exceptions/")
    time.sleep(3)
    
    # Maximize the window
    driver.maximize_window()
    time.sleep(3)

    # Wait for and click on the "Contact" menu
    contact_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Contact')]"))
    )
    time.sleep(3)
    contact_link.click()

    # Wait for page to load and verify URL
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.url_matches("https://practicetestautomation.com/contact/"))
    current_url = driver.current_url

    # Assert the URL
    if current_url == "https://practicetestautomation.com/contact/":
        sys.exit(0)  # Exit code 0 for success
    else:
        sys.exit(1)  # Exit code 1 for failure

except Exception as e:
    print(f"Test case failed: {e}")
    sys.exit(1)  # Exit code 1 for failure

finally:
    # Clean up
    driver.quit()
