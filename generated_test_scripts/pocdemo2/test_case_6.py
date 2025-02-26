
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

def test_ui():
    # Setting up Chrome options
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-notifications')
    options.add_argument('--incognito')
    options.add_argument('--disable-features=NetworkService')
    options.add_argument('--disable-gpu')

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=options)

    try:
        # Step 1: Navigate to the homepage
        driver.maximize_window()
        driver.get("https://practicetestautomation.com/")
        time.sleep(5)

        # Step 2: Click on the "Courses" menu
        time.sleep(3)
        courses_menu = driver.find_element(By.XPATH, "//a[contains(text(),'Courses')]")
        courses_menu.click()

        # Step 3: Wait for the page to load
        time.sleep(3)

        # Step 4: Verify the page URL
        time.sleep(3)
        current_url = driver.current_url
        assert current_url == "https://practicetestautomation.com/courses/"

        # If the test case passes
        sys.exit(0)

    except AssertionError:
        # If the test case fails
        sys.exit(1)
    
    finally:
        # Clean up
        driver.quit()

if __name__ == "__main__":
    test_ui()
