
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import sys

def main():
    # Chrome options setup
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")

    # Initialize WebDriver
    driver = webdriver.Chrome(options=options)

    try:
        # Maximize the page
        driver.maximize_window()

        # Navigate to the homepage
        driver.get("https://practicetestautomation.com")
        time.sleep(5)

        # Click on the "Contact" menu
        contact_link = driver.find_element(By.XPATH, "//a[contains(text(),'Contact')]")
        time.sleep(3)
        contact_link.click()

        # Wait for the page to load
        driver.implicitly_wait(10)

        # Verify that the page URL is correct
        time.sleep(3)
        current_url = driver.current_url
        if current_url == "https://practicetestautomation.com/contact/":
            print("Test Passed: URL is correct.")
            sys.exit(0)
        else:
            print("Test Failed: URL is incorrect.")
            sys.exit(1)

    except Exception as e:
        print(f"Test Failed: {e}")
        sys.exit(1)

    finally:
        # Close the driver
        driver.quit()

if __name__ == "__main__":
    main()
