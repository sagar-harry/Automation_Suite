
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_navigate_to_courses():
    try:
        # Set up Chrome options
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--incognito")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-features=NetworkService")
        
        # Initialize WebDriver
        driver = webdriver.Chrome(options=options)
        
        # Open the homepage
        driver.get("https://practicetestautomation.com")
        time.sleep(5)
        
        # Maximize the window
        driver.maximize_window()
        
        # Wait for 3 seconds before each action
        time.sleep(3)
        
        # Click on the "Courses" menu
        courses_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Courses')]"))
        )
        courses_link.click()
        
        # Wait for 3 seconds to let the page load
        time.sleep(3)
        
        # Verify the page URL
        expected_url = "https://practicetestautomation.com/courses/"
        actual_url = driver.current_url
        assert actual_url == expected_url, f"URL mismatch: expected {expected_url}, got {actual_url}"
        
        driver.quit()
        sys.exit(0)
        
    except Exception as e:
        print("Test Case Failed: ", e)
        if driver:
            driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    test_navigate_to_courses()
