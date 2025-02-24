
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_practice_menu_navigation():
    options = Options()
    options.headless = True
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popups")
    options.add_argument("--disable-features=NetworkService")
    
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    try:
        # Navigate to homepage
        driver.get('https://practicetestautomation.com')
        time.sleep(5)  # Wait for the page to load

        # Click on the "Practice" menu
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Practice')]"))
        )
        time.sleep(3)  # Additional wait before clicking
        practice_menu = driver.find_element(By.XPATH, "//a[contains(text(),'Practice')]")
        practice_menu.click()
        time.sleep(3)  # Additional wait after clicking to ensure page load

        # Verify that the page URL is as expected
        WebDriverWait(driver, 10).until(
            EC.url_to_be('https://practicetestautomation.com/practice/')
        )
        time.sleep(3)  # Additional wait before verification

        assert driver.current_url == 'https://practicetestautomation.com/practice/'
        driver.quit()
        sys.exit(0)  # Exit with code 0 if test case passed
    except Exception as e:
        print(f"Test failed: {e}")
        driver.quit()
        sys.exit(1)  # Exit with code 1 if test case failed

if __name__ == "__main__":
    test_practice_menu_navigation()
