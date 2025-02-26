
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_ui_navigation():
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-features=NetworkService")

    # Start the webdriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Maximize window
        driver.maximize_window()

        # Navigate to the homepage
        driver.get("https://practicetestautomation.com/")
        time.sleep(5)  # Wait for 5 seconds after opening the page

        # Wait before action and then click on the "Courses" menu
        time.sleep(3)
        courses_menu = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Courses')]"))
        )
        courses_menu.click()

        # Wait for the page to load
        time.sleep(3)

        # Verify that the page URL is correct
        current_url = driver.current_url
        if current_url == "https://practicetestautomation.com/courses/":
            sys.exit(0)
        else:
            sys.exit(1)

    except Exception as e:
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    test_ui_navigation()
