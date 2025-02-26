
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

try:
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-features=NetworkService")
    
    # Initialize the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)
    
    # Maximize the browser window
    driver.maximize_window()

    # Navigate to the homepage
    driver.get("https://practicetestautomation.com/")
    
    # Wait after opening the page
    time.sleep(5)

    # Locate and click on the "Courses" menu
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Courses')]"))
    )
    time.sleep(3)
    driver.find_element(By.XPATH, "//a[contains(text(),'Courses')]").click()

    # Wait for the page to load and verify the URL
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://practicetestautomation.com/courses/")
    )
    
    # Capture screenshot of the page
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\courses_page.png")

    # Exit with success
    sys.exit(0)

except Exception as e:
    # Print the exception, capture screenshot, and exit with failure
    print(f"Test failed: {e}")
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error_page.png")
    sys.exit(1)

finally:
    # Ensure driver is closed
    driver.quit()
