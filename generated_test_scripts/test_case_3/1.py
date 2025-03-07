
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from compare_sentences import compare_sentences

def test_checkout_process():
    # Set options for Chrome
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")

    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(options=options)

    try:
        wait_time = 3

        # Step 1: Open the SauceDemo website
        driver.get("https://saucedemo.com/")
        driver.maximize_window()
        time.sleep(wait_time)

        # Step 2: Find the username input field and enter 'standard_user'
        username_input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='user-name']"))
        )
        username_input_field.send_keys("standard_user")
        time.sleep(wait_time)

        # Step 3: Find the password input field and enter 'secret_sauce'
        password_input_field = driver.find_element(By.XPATH, "//input[@id='password']")
        password_input_field.send_keys("secret_sauce")
        time.sleep(wait_time)

        # Step 4: Find the login button and click it
        login_button = driver.find_element(By.XPATH, "//input[@data-test='login-button']")
        login_button.click()
        time.sleep(wait_time)

        # Step 5: Verify redirection to the Product Listing Page with URL '/inventory.html'
        WebDriverWait(driver, 10).until(
            EC.url_contains("/inventory.html")
        )
        assert compare_sentences(driver.current_url, "https://saucedemo.com/inventory.html"), "Failed to redirect to Product Listing Page"

        # Step 6: Click the Cart Icon
        cart_icon = driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']")
        cart_icon.click()
        time.sleep(wait_time)

        # Step 7: Verify redirection to Shopping Cart Page with URL '/cart.html'
        WebDriverWait(driver, 10).until(
            EC.url_contains("/cart.html")
        )
        assert compare_sentences(driver.current_url, "https://saucedemo.com/cart.html"), "Failed to redirect to Shopping Cart Page"

        # Step 8: Click the 'Checkout' button
        checkout_button = driver.find_element(By.XPATH, "//button[@data-test='checkout']")
        checkout_button.click()
        time.sleep(wait_time)

        # Step 9: Verify redirection to Checkout Step 1: User Info page with URL '/checkout-step-one.html'
        WebDriverWait(driver, 10).until(
            EC.url_contains("/checkout-step-one.html")
        )
        assert compare_sentences(driver.current_url, "https://saucedemo.com/checkout-step-one.html"), "Failed to redirect to Checkout Step 1: User Info page"

        sys.exit(0)

    except Exception as e:
        print(f"Test failed due to: {e}")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    test_checkout_process()
