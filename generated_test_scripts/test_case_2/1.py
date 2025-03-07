
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
from compare_sentences import compare_sentences

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--start-maximized")

# Start WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Step 1: Navigate to Login Page
    driver.get("https://www.saucedemo.com/")

    time.sleep(3)

    # Step 2: Ensure the login form is present
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@data-test='username']"))
    )
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@data-test='password']"))
    )

    # Step 3 & 4: Enter username and password
    driver.find_element(By.XPATH, "//input[@data-test='username']").send_keys("standard_user")
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@data-test='password']").send_keys("secret_sauce")
    time.sleep(3)

    # Step 5: Click the Login button
    driver.find_element(By.XPATH, "//input[@data-test='login-button']").click()

    time.sleep(3)

    # Step 6: Verify redirection to the Product Listing Page
    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )
    current_url = driver.current_url
    expected_url = "https://www.saucedemo.com/inventory.html"
    if not compare_sentences(current_url, expected_url):
        raise ValueError(f"URL mismatch: {current_url} != {expected_url}")

    # Step 7: Click 'Add to Cart' for 'Sauce Labs Backpack'
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']"))
    ).click()

    time.sleep(3)

    # Step 8: Check cart count update
    cart_count_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']"))
    )
    cart_count = cart_count_element.text
    expected_count = "1"
    if not compare_sentences(cart_count, expected_count):
        raise ValueError(f"Cart count mismatch: {cart_count} != {expected_count}")

    # If everything went well, exit with code 0
    sys.exit(0)
except Exception as e:
    print(f"Test failed: {str(e)}")
    sys.exit(1)
finally:
    # Quit the driver
    driver.quit()
