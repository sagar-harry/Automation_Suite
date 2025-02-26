
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def test_add_items_to_cart():
    screenshot_directory = "C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots"
    script_name = os.path.splitext(os.path.basename(__file__))[0]

    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-features=NetworkService")

    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    try:
        # Open the website
        driver.get("https://saucedemo.com/")
        time.sleep(5)  # Wait for 5 seconds after opening the page

        # Login to the website
        login_to_website(driver, "standard_user", "secret_sauce")

        # Add 'Bike Light' to the cart
        wait_for_element_and_click(driver, By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')

        # Add 'Fleece Jacket' to the cart
        wait_for_element_and_click(driver, By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')

        # Verify the cart count
        cart_count = wait_for_element(driver, By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
        if cart_count == '2':
            sys.exit(0)  # Test case passed
        else:
            sys.exit(1)  # Test case failed

    finally:
        # Save a screenshot before closing
        driver.save_screenshot(os.path.join(screenshot_directory, f"{script_name}_screenshot.png"))
        driver.quit()

def login_to_website(driver, username, password):
    # Wait for and fill username
    wait_for_element_and_send_keys(driver, By.XPATH, '//*[@id="user-name"]', username)
    
    # Wait for and fill password
    wait_for_element_and_send_keys(driver, By.XPATH, '//*[@id="password"]', password)
    
    # Wait for and click login button
    wait_for_element_and_click(driver, By.XPATH, '//*[@id="login-button"]')

def wait_for_element(driver, by, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, locator)))

def wait_for_element_and_click(driver, by, locator):
    element = wait_for_element(driver, by, locator)
    time.sleep(3)  # Wait for 3 seconds before action
    element.click()

def wait_for_element_and_send_keys(driver, by, locator, keys):
    element = wait_for_element(driver, by, locator)
    time.sleep(3)  # Wait for 3 seconds before action
    element.send_keys(keys)

# Run the test
if __name__ == "__main__":
    test_add_items_to_cart()
