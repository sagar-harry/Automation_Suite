
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from compare_sentences import compare_sentences
import sys

options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_argument("--incognito")
options.add_argument("--start-maximized")

def validate_cart_count():
    driver = webdriver.Chrome(options=options)
    try:
        # Navigate to the login page
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        
        # Wait for the username field to appear and enter the username
        username_field = driver.find_element(By.XPATH, "//input[@data-test='username']")
        username_field.send_keys("standard_user")
        time.sleep(3)
        
        # Wait for the password field to appear and enter the password
        password_field = driver.find_element(By.XPATH, "//input[@data-test='password']")
        password_field.send_keys("secret_sauce")
        time.sleep(3)
        
        # Wait for the login button to be clickable and click it
        login_button = driver.find_element(By.XPATH, "//input[@data-test='login-button']")
        login_button.click()
        time.sleep(3)
        
        # Verify we are on the Product Listing page
        current_url = driver.current_url
        if not compare_sentences(current_url, "https://www.saucedemo.com/inventory.html"):
            raise AssertionError("Did not navigate to the Product Listing page.")
        
        # Wait for the 'Add to cart' button to appear and click it
        add_to_cart_button = driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']")
        add_to_cart_button.click()
        time.sleep(3)
        
        # Verify the cart count increment in the 'Shopping Cart Badge'
        shopping_cart_badge = driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']/span")
        cart_count_text = shopping_cart_badge.text
        
        if not compare_sentences(cart_count_text, "1"):
            raise AssertionError(f"Cart count is incorrect, expected '1' but got '{cart_count_text}'.")

        sys.exit(0)

    except Exception as e:
        print(f"Test failed: {str(e)}")
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    validate_cart_count()
