
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_ui_navigation():
    try:
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-features=NetworkService")

        # Create a WebDriver instance
        driver = webdriver.Chrome(options=chrome_options)
        
        # Maximize the browser window
        driver.maximize_window()

        # Navigate to the homepage
        driver.get("https://practicetestautomation.com/")
        time.sleep(5)  # Wait for the page to fully load

        # Wait before performing further actions
        time.sleep(3)

        # Click on the "Practice" menu
        practice_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Practice')]"))
        )
        practice_menu.click()

        # Wait before performing further actions
        time.sleep(3)

        # Wait for the page to load and check the URL
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://practicetestautomation.com/practice/")
        )

        # Assert the page URL
        assert driver.current_url == "https://practicetestautomation.com/practice/"

        # Close the browser
        driver.quit()

        # Exit with code 0 if the test is successful
        exit(0)

    except Exception as e:
        print(f"Test failed: {str(e)}")
        
        # Exit with code 1 if the test fails
        exit(1)

if __name__ == "__main__":
    test_ui_navigation()
