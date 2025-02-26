
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    # Chrome options setup
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=NetworkService")

    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    # Maximize the window
    driver.maximize_window()

    # Step 1: Navigate to homepage
    driver.get("https://practicetestautomation.com/")
    time.sleep(5)  # Wait after page load

    # Step 2: Click on the "Home" menu
    home_menu = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Home')]"))
    )
    time.sleep(3)  # Additional wait before action
    home_menu.click()

    # Step 3: Wait for the page to load
    time.sleep(3)  # Additional wait after click

    # Step 4: Verify the URL
    current_url = driver.current_url
    if current_url != "https://practicetestautomation.com/":
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\failed.png")
        raise Exception("URL did not match the expected value.")
    
    # Save screenshot
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\passed.png")

    # Close the driver
    driver.quit()

    # Exit with success
    sys.exit(0)

except Exception as e:
    print(f"Test case failed: {e}")
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error.png")
    driver.quit()
    sys.exit(1)
