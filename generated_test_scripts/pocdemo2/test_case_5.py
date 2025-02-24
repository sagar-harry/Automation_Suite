
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

# Configure Chrome options for headless mode, incognito, and disabling notifications
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-features=NetworkService")
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Navigate to the homepage
    driver.get("https://practicetestautomation.com/")
    driver.maximize_window()

    # Wait 5 seconds after opening the page
    time.sleep(5)

    # Click on the "Practice" menu
    practice_menu = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Practice')]"))
    )
    time.sleep(3)
    practice_menu.click()

    # Wait for the page to load and verify the URL
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://practicetestautomation.com/practice/")
    )

    # Test case passed
    sys.exit(0)

except Exception as e:
    # Test case failed
    print(f"Test case failed: {e}")
    sys.exit(1)

finally:
    # Close the driver
    driver.quit()
