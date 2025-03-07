
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import sys
from compare_sentences import compare_sentences

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--start-maximized")

# Create a new Chrome session
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.saucedemo.com")
sleep(3)

try:
    # Step 1: Login Page
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='user-name']"))
    )
    username_input = driver.find_element(By.XPATH, "//input[@id='user-name']")
    password_input = driver.find_element(By.XPATH, "//input[@id='password']")
    login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
    
    sleep(3)
    username_input.send_keys("standard_user")
    sleep(3)
    password_input.send_keys("secret_sauce")
    sleep(3)
    login_button.click()
    
    # Step 5: Verify redirection to Product Listing Page
    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )
    
    # Step 6: Add product to cart
    add_to_cart_button = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    sleep(3)
    add_to_cart_button.click()

    # Step 7: Go to Cart
    cart_icon = driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']")
    sleep(3)
    cart_icon.click()
    
    # Step 8: Verify Shopping Cart Page
    WebDriverWait(driver, 10).until(
        EC.url_contains("cart.html")
    )

    # Step 9: Verify product in cart
    product_in_cart = driver.find_element(By.XPATH, "//div[@class='inventory_item_name']").text
    assert compare_sentences(product_in_cart, "Sauce Labs Backpack")

    # Step 10: Checkout
    checkout_button = driver.find_element(By.XPATH, "//button[@id='checkout']")
    sleep(3)
    checkout_button.click()

    # Step 11: Verify navigation to Checkout Step 1
    WebDriverWait(driver, 10).until(
        EC.url_contains("/checkout-step-one.html")
    )

    # Step 12: Fill in details and continue
    first_name_input = driver.find_element(By.XPATH, "//input[@id='first-name']")
    last_name_input = driver.find_element(By.XPATH, "//input[@id='last-name']")
    zip_code_input = driver.find_element(By.XPATH, "//input[@id='postal-code']")
    continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
    
    sleep(3)
    first_name_input.send_keys("John")
    sleep(3)
    last_name_input.send_keys("Doe")
    sleep(3)
    zip_code_input.send_keys("12345")
    sleep(3)
    continue_button.click()

    # Step 13: Verify Checkout Step 2
    WebDriverWait(driver, 10).until(
        EC.url_contains("/checkout-step-two.html")
    )

    # Step 14: Verify order details
    order_total_element = driver.find_element(By.XPATH, "//div[@class='summary_total_label']")
    order_total_text = order_total_element.text
    assert compare_sentences(order_total_text, "Total: $32.39")

    # Step 15: Finish Order
    finish_button = driver.find_element(By.XPATH, "//button[@id='finish']")
    sleep(3)
    finish_button.click()

    # Step 16: Verify order confirmation
    WebDriverWait(driver, 10).until(
        EC.url_contains("/checkout-complete.html")
    )
    
    # Step 17: Verify confirmation message
    confirmation_message = driver.find_element(By.XPATH, "//h2[@data-test='complete-header']").text
    assert compare_sentences(confirmation_message, "Thank you for your order!")

    sys.exit(0)
except Exception as e:
    print(f"Test failed: {e}")
    sys.exit(1)
finally:
    driver.quit()
