
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import sys

def test_courses_page():
    try:
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument('--disable-popup-blocking')
        chrome_options.add_argument('--incognito')
        chrome_options.add_argument('--disable-features=NetworkService')

        driver = webdriver.Chrome(options=chrome_options)
        
        driver.maximize_window()
        time.sleep(3)  # Wait before navigating
        
        driver.get("https://practicetestautomation.com")
        time.sleep(5)  # Wait for the page to load

        # Click on the "Courses" menu
        courses_menu = driver.find_element(By.XPATH, "//a[contains(text(),'Courses')]")
        courses_menu.click()
        time.sleep(3)  # Wait after click

        # Wait for the page to load
        driver.implicitly_wait(10)
        
        # Verify the page URL
        expected_url = "https://practicetestautomation.com/courses/"
        current_url = driver.current_url

        if current_url == expected_url:
            print("Test Passed")
            sys.exit(0)
        else:
            print("Test Failed")
            sys.exit(1)

    except Exception as e:
        print(f"An exception occurred: {str(e)}")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    test_courses_page()
