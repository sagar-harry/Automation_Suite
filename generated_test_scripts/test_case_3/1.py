
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys
from compare_sentences import compare_sentences

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("--disable-notifications")

try:
    # Initialize the driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    
    # Helper function to wait for 3 seconds before each action
    def wait_and_find_element(by, value):
        time.sleep(3)
        return driver.find_element(by, value)

    # Step 1: Navigate to the Login Page
    driver.get("https://www.saucedemo.com/")
    
    # Step 2: Check presence of login form fields
    username_field = wait_and_find_element(By.XPATH, "//input[@id='user-name']")
    password_field = wait_and_find_element(By.XPATH, "//input[@id='password']")
    
    # Step 3 & 4: Enter username and password
    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    
    # Step 5: Click login button
    login_button = wait_and_find_element(By.XPATH, "//input[@id='login-button']")
    login_button.click()
    
    # Step 6: Validate redirection to the Product Listing Page
    time.sleep(3)
    assert driver.current_url.endswith("/inventory.html")
    
    # Step 7: Add Sauce Labs Backpack to cart
    add_to_cart_button = wait_and_find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    add_to_cart_button.click()
    
    # Step 8: Navigate to the shopping cart
    cart_icon = wait_and_find_element(By.XPATH, "//a[@data-test='shopping-cart-link']")
    cart_icon.click()
    
    # Step 9: Validate redirection to the Shopping Cart Page
    time.sleep(3)
    assert driver.current_url.endswith("/cart.html")
    
    # Step 10: Ensure 'Your Cart' title is displayed
    your_cart_title = wait_and_find_element(By.XPATH, "//span[@data-test='title'][text()='Your Cart']")
    assert compare_sentences(your_cart_title.text, "Your Cart")
    
    # Step 11: Begin Checkout
    checkout_button = wait_and_find_element(By.XPATH, "//button[@id='checkout']")
    checkout_button.click()
    
    # Step 12: Validate redirection to Checkout Step 1 Page
    time.sleep(3)
    assert driver.current_url.endswith("/checkout-step-one.html")
    
    # Step 13: Confirm "Checkout: Your Information" title
    checkout_your_info_title = wait_and_find_element(By.XPATH, "//span[@data-test='title'][text()='Checkout: Your Information']")
    assert compare_sentences(checkout_your_info_title.text, "Checkout: Your Information")
    
    # Step 14: Enter checkout information
    first_name_field = wait_and_find_element(By.XPATH, "//input[@id='first-name']")
    last_name_field = wait_and_find_element(By.XPATH, "//input[@id='last-name']")
    postal_code_field = wait_and_find_element(By.XPATH, "//input[@id='postal-code']")
    
    first_name_field.send_keys("firstName")
    last_name_field.send_keys("lastName")
    postal_code_field.send_keys("postalCode")
    
    # Step 15: Click Continue button
    continue_button = wait_and_find_element(By.XPATH, "//input[@id='continue']")
    continue_button.click()
    
    # Step 16: Validate redirection to Checkout Step 2 Overview Page
    time.sleep(3)
    assert driver.current_url.endswith("/checkout-step-two.html")
    
    # Step 17: Ensure "Checkout: Overview" title is displayed
    checkout_overview_title = wait_and_find_element(By.XPATH, "//span[@data-test='title'][text()='Checkout: Overview']")
    assert compare_sentences(checkout_overview_title.text, "Checkout: Overview")
    
    # Step 18: Click Finish button
    finish_button = wait_and_find_element(By.XPATH, "//button[@id='finish']")
    finish_button.click()
    
    # Step 19: Validate redirection to Order Confirmation Page
    time.sleep(3)
    assert driver.current_url.endswith("/checkout-complete.html")
    
    # Step 20: Confirm "Thank you for your order!" message
    thank_you_message = wait_and_find_element(By.XPATH, "//h2[@class='complete-header'][text()='Thank you for your order!']")
    assert compare_sentences(thank_you_message.text, "Thank you for your order!")

    # If all steps pass
    print("Test Case Passed")
    sys.exit(0)

except Exception as e:
    print(f"Test Case Failed: {e}")
    sys.exit(1)

finally:
    # Ensure driver quits even in case of failure
    driver.quit()
