
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuring Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-features=NetworkService")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Navigate to the website
    driver.get("https://saucedemo.com/")
    time.sleep(5)  # Wait for 5 seconds as per spec
    driver.maximize_window()

    # Login
    from LoginPage import login

    login(driver, "standard_user", "secret_sauce")
    time.sleep(3)  # Wait for 3 seconds before next action
    
    # Add 'Bike Light' to the cart
    bike_light = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
    )
    bike_light.click()
    time.sleep(3)  # Wait for 3 seconds before next action

    # Add 'Fleece Jacket' to the cart
    fleece_jacket = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
    )
    fleece_jacket.click()
    time.sleep(3)  # Wait for 3 seconds before next action

    # Verify cart badge count
    cart_count_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
    )
    cart_count = cart_count_element.text

    assert cart_count == "2", f"Cart count is incorrect, expected 2 but got {cart_count}"

    # Save Screenshot
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\cart_verification.png")

    # If no exceptions, exit with success
    sys.exit(0)

except Exception as e:
    print(f"Test failed: {e}")
    sys.exit(1)

finally:
    driver.quit()
