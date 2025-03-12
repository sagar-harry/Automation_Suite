
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Locator constants
USERNAME_LOCATOR = "//*[@id='user-name']"
PASSWORD_LOCATOR = "//*[@id='password']"
LOGIN_BUTTON_LOCATOR = "//*[@id='login-button']"
BIKE_LIGHT_LOCATOR = "//*[@id='add-to-cart-sauce-labs-bike-light']"
FLEECE_JACKET_LOCATOR = "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
CART_COUNT_LOCATOR = "//*[@id='shopping_cart_container']/a/span"

# Initialize Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-features=NetworkService")

try:
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    # Navigate to the website
    driver.get("https://saucedemo.com/")
    time.sleep(5)  # wait for page to load completely

    # Function to login
    def login_to_saucedemo():
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, USERNAME_LOCATOR))).send_keys("standard_user")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, PASSWORD_LOCATOR))).send_keys("secret_sauce")
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, LOGIN_BUTTON_LOCATOR))).click()
        time.sleep(3)
    
    # Login to the application
    login_to_saucedemo()
    
    # Add items to the cart
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, BIKE_LIGHT_LOCATOR))).click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, FLEECE_JACKET_LOCATOR))).click()
    time.sleep(3)

    # Verify cart count
    cart_count_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, CART_COUNT_LOCATOR)))
    cart_count = cart_count_element.text.strip()

    # Verify cart badge display count
    assert cart_count == "2", f"Expected cart count to be 2, but got {cart_count}"

    # Save the snapshot of the page
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\cart_verification.png")

    # Test passed
    sys.exit(0)

except Exception as e:
    print(f"Test case failed: {str(e)}")
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\cart_verification_failed.png")
    sys.exit(1)

finally:
    driver.quit()
