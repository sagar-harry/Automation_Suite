
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    # Set Chrome Options
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup")
    chrome_options.add_argument("--disable-features=NetworkService")

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    
    # Maximize the window
    driver.maximize_window()
    
    # Open the homepage
    driver.get("https://practicetestautomation.com/")
    time.sleep(5)
    
    # Click on the "Practice" menu
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Practice')]"))
    )
    time.sleep(3)
    practice_menu = driver.find_element(By.XPATH, "//a[contains(text(),'Practice')]")
    practice_menu.click()
    
    # Wait for the Practice page to load
    time.sleep(3)
    
    # Verify the page URL
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://practicetestautomation.com/practice/")
    )
    
    # Save screenshot
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
    
    # Close the driver
    driver.quit()
    
    # Exit with success code
    sys.exit(0)

except Exception as e:
    print(f"Test failed due to: {str(e)}")
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\failure_screenshot.png")
    driver.quit()
    sys.exit(1)
