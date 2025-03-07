
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-features=NetworkService")

try:
    # Initialize the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)
    
    # Open the website
    driver.get("https://saucedemo.com/")
    time.sleep(5)

    # Maximize the browser window
    driver.maximize_window()

    # Login to the website
    driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys("standard_user")
    time.sleep(3)

    driver.find_element(By.XPATH, "//*[@id='password']").send_keys("secret_sauce")
    time.sleep(3)

    driver.find_element(By.XPATH, "//*[@id='login-button']").click()

    # Wait for elements to appear and add 'Bike Light' to cart
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']"))
    ).click()
    time.sleep(3)

    # Add 'Fleece Jacket' to cart
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']"))
    ).click()
    time.sleep(3)

    # Verify cart badge displays '2'
    cart_badge = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='shopping_cart_container']/a/span"))
    ).text
    assert cart_badge == '2', f"Expected cart badge '2', but got {cart_badge}"

    # Save a snapshot of the page
    os.makedirs(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots", exist_ok=True)
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\test_case_result.png")

    # Exit test successfully
    driver.quit()
    sys.exit(0)

except Exception as e:
    if 'driver' in locals():
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\test_case_result.png")
        driver.quit()
    print(f"Test case failed: {e}")
    sys.exit(1)
