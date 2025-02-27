
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

# Set Chrome options
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_argument("--incognito")
options.add_argument("--disable-features=NetworkService")

# Initialize WebDriver
driver = webdriver.Chrome(options=options)

try:
    # Navigate to the homepage
    driver.get("https://practicetestautomation.com/")
    driver.maximize_window()
    time.sleep(5)  # Delay to ensure the page loads

    # Click on the "Practice" menu
    time.sleep(3)
    practice_menu = driver.find_element(By.XPATH, "//a[contains(text(),'Practice')]")
    practice_menu.click()
    time.sleep(3)

    # Verify the URL
    time.sleep(3)
    current_url = driver.current_url
    if current_url == "https://practicetestautomation.com/practice/":
        print("Test case passed.")
        sys.exit(0)
    else:
        print("Test case failed: Incorrect URL")
        sys.exit(1)

except Exception as e:
    print(f"Test case failed: Exception {e}")
    sys.exit(1)

finally:
    driver.quit()
