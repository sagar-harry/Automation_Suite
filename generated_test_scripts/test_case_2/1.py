
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from compare_sentences import compare_sentences

def run_test():
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup")
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    
    try:
        # Step 1: Open the SauceDemo website
        driver.get("https://saucedemo.com/")
        time.sleep(3)

        # Step 2: Find the username input field by ID 'user-name' and enter 'standard_user'
        username_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='user-name']")))
        username_field.send_keys("standard_user")
        time.sleep(3)

        # Step 3: Find the password input field by ID 'password' and enter 'secret_sauce'
        password_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password']")))
        password_field.send_keys("secret_sauce")
        time.sleep(3)

        # Step 4: Find the login button by data-test attribute 'login-button' and click it
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@data-test='login-button']")))
        login_button.click()
        time.sleep(3)
        
        # Step 5: Verify redirection to the Product Listing Page with URL '/inventory.html'
        wait.until(EC.url_contains("/inventory.html"))
        actual_url = driver.current_url
        expected_url = "https://www.saucedemo.com/inventory.html"
        if compare_sentences(actual_url, expected_url):
            print("Redirection to Product Listing Page verified.")
        else:
            print("Redirection to Product Listing Page failed.")
            sys.exit(1)
        
        # Step 6: Click the 'Add to cart' button for an item using the data-test attribute 'add-to-cart-sauce-labs-backpack'
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']")))
        add_to_cart_button.click()
        time.sleep(3)

        # Step 7: Verify the shopping cart icon shows a badge indicating one item is added by checking the class 'shopping_cart_badge'
        cart_badge = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']")))
        actual_badge_count = cart_badge.text
        expected_badge_count = "1"
        if compare_sentences(actual_badge_count, expected_badge_count):
            print("Shopping cart badge correctly shows 1 item.")
            sys.exit(0)
        else:
            print("Shopping cart badge verification failed.")
            sys.exit(1)
    
    finally:
        driver.quit()

if __name__ == '__main__':
    run_test()
