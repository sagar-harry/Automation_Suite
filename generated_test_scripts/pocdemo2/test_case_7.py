
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

def test_blog_navigation():
    chrome_options = Options()
    # Run in headless mode
    chrome_options.add_argument("--headless")
    # Disable notifications, pop-ups, and run in incognito mode
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--incognito")
    # Disable NetworkService feature
    chrome_options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=chrome_options)
    try:
        # Maximize page and set timeouts
        driver.maximize_window()
        driver.implicitly_wait(5)

        # Navigate to homepage
        driver.get("https://practicetestautomation.com/")
        time.sleep(5)  # Wait for 5 seconds after opening the page
        
        # Click on the "Blog" menu
        time.sleep(3)  # Wait for 3 seconds before action
        blog_menu = driver.find_element(By.XPATH, "//a[contains(text(),'Blog')]")
        blog_menu.click()
        
        # Wait for the page to load
        time.sleep(5)  # Wait for 5 seconds after click
        
        # Verify the URL
        time.sleep(3)  # Wait for 3 seconds before verification
        if driver.current_url == "https://practicetestautomation.com/blog/":
            sys.exit(0)  # Exit with code 0 if the test case passed
        else:
            sys.exit(1)  # Exit with code 1 if the test case failed
    except Exception as e:
        sys.exit(1)
    finally:
        driver.quit()

test_blog_navigation()
