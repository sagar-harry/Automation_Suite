
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time
import os

try:
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=NetworkService")

    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    # Open website and maximize window
    driver.get("https://saucedemo.com/")
    time.sleep(5)  # Wait for 5 seconds after opening the page
    driver.maximize_window()

    # Define explicit wait
    wait = WebDriverWait(driver, 10)

    # Log in
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))).send_keys('standard_user')
    time.sleep(3)
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys('secret_sauce')
    time.sleep(3)
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-button"]'))).click()
    time.sleep(3)

    # Add items to cart
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
    time.sleep(3)
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]'))).click()
    time.sleep(3)

    # Verify cart badge for '2' items
    badge = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
    if badge.text != '2':
        raise Exception("Cart badge did not display '2' after adding items")

    # Remove items
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]'))).click()
    time.sleep(3)
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]'))).click()
    time.sleep(3)

    # Verify cart count element does not exist
    try:
        wait.until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
    except:
        raise Exception("Cart count element still exists after removing items")

    # Add Bolt T-Shirt to cart
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
    time.sleep(3)

    # Verify cart badge for '1' item
    badge = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
    if badge.text != '1':
        raise Exception("Cart badge did not display '1' after adding Bolt T-Shirt")

    # Capture screenshot
    screenshot_path = os.path.join("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots", "test_screenshot.png")
    driver.save_screenshot(screenshot_path)

    # Exit with success
    sys.exit(0)

except Exception as e:
    print(f"Test failed due to exception: {e}")

finally:
    # Close the browser
    if driver:
        driver.quit()
    
    # Exit with failure
    sys.exit(1)
