
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import sys
from compare_sentences import compare_sentences

# Configuration for Chrome browser
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--start-maximized")

# Locators
login_page_username_field_xpath = "//input[@data-test='username']"
login_page_password_field_xpath = "//input[@data-test='password']"
login_page_login_button_xpath = "//input[@data-test='login-button']"
product_listing_page_add_to_cart_xpath = "//button[@data-test='add-to-cart-sauce-labs-backpack']"
product_listing_page_shopping_cart_xpath = "//a[@data-test='shopping-cart-link']"
cart_page_cart_badge_xpath = "//span[@data-test='shopping-cart-badge']"

try:
    # Setup WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://saucedemo.com/")

    # Step 1: Open the SauceDemo login page
    # The page is already loaded as we visited the URL above
    sleep(3)  # Waiting for 3 seconds

    # Step 2 & 3: Enter the username and password
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, login_page_username_field_xpath))).send_keys("standard_user")
    sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, login_page_password_field_xpath))).send_keys("secret_sauce")
    sleep(3)

    # Step 4: Click the login button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, login_page_login_button_xpath))).click()
    sleep(3)

    # Step 5: Ensure redirection to the product listing page
    WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))
    product_list_url = driver.current_url
    expected_product_list_url = "https://www.saucedemo.com/inventory.html"
    assert compare_sentences(product_list_url, expected_product_list_url), "URLs do not match!"

    # Step 6: Click on the 'Add to cart' button for a product
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, product_listing_page_add_to_cart_xpath))).click()
    sleep(3)

    # Step 7: Verify the cart icon shows a count of 1
    cart_badge = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, cart_page_cart_badge_xpath)))
    expected_cart_count = "1"
    assert compare_sentences(cart_badge.text, expected_cart_count), "Cart count does not match expected value!"

    print("Test case passed.")
    sys.exit(0)

except Exception as e:
    print(f"Test case failed: {e}")
    sys.exit(1)

finally:
    driver.quit()
