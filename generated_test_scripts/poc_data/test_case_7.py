
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_blog_navigation():
    # Set up Chrome options for headless mode, incognito, and disable notifications
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-features=NetworkService")

    # Initialize the webdriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Navigate to the homepage
        driver.get("https://practicetestautomation.com")
        time.sleep(5)  # Wait for 5 secs after opening the page

        # Maximize the browser window
        driver.maximize_window()

        # Wait and click on the "Blog" menu
        time.sleep(3)
        blog_menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Blog')]"))
        )
        blog_menu.click()

        # Wait for the page to load
        time.sleep(3)  # Wait for additional 3 seconds after click

        # Verify that the page URL is https://practicetestautomation.com/blog/
        expected_url = "https://practicetestautomation.com/blog/"
        current_url = driver.current_url
        if current_url == expected_url:
            print("Test Passed: URL is correct")
            sys.exit(0)
        else:
            print("Test Failed: URL is incorrect")
            sys.exit(1)
    except Exception as e:
        print(f"Test Failed due to an exception: {e}")
        sys.exit(1)
    finally:
        # Close the browser
        driver.quit()

test_blog_navigation()
