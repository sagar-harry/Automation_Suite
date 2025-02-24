
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import sys

def test_contact_page():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=NetworkService")

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # Maximize window
        driver.maximize_window()
        
        # Navigate to homepage
        driver.get("https://practicetestautomation.com/")
        time.sleep(5)  # Wait for page to load
        
        # Locate and click on the "Contact" menu
        contact_menu = driver.find_element(By.XPATH, "//a[contains(text(),'Contact')]")
        time.sleep(3)  # Wait before action
        contact_menu.click()
        
        # Wait for the page to load
        time.sleep(5)
        
        # Verify the page URL
        if driver.current_url == "https://practicetestautomation.com/contact/":
            print("Test Passed")
            sys.exit(0)
        else:
            print("Test Failed: URL mismatch.")
            sys.exit(1)
    except Exception as e:
        print(f"Test Failed: {str(e)}")
        sys.exit(1)
    finally:
        # Close the browser
        driver.quit()

test_contact_page()
