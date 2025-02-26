
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

def test_ui_scenario():
    try:
        # Setting up Chrome Options
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-notifications')
        options.add_argument('--incognito')
        options.add_argument('--disable-features=NetworkService')
        options.add_argument('--window-size=1920,1080') # maximizes the page
        
        driver = webdriver.Chrome(options=options)
        
        # Navigate to the homepage
        driver.get("https://practicetestautomation.com/")
        time.sleep(5)

        # Wait for 3 seconds
        time.sleep(3)

        # Click on the "Practice" menu
        practice_menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Practice')]"))
        )
        practice_menu.click()

        # Wait for page load
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://practicetestautomation.com/practice/")
        )
        
        # Verify that the page URL is correct
        assert driver.current_url == "https://practicetestautomation.com/practice/"
        
        print("Test Case Passed")
        sys.exit(0)
    except Exception as e:
        print(f"Test Case Failed: {e}")
        sys.exit(1)
    finally:
        # Close the browser
        driver.quit()

test_ui_scenario()
