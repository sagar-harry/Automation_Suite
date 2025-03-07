
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from compare_sentences import compare_sentences
import time
import sys

def test_checkout_process():
    # Setting up Chrome options for incognito mode and disabling notifications
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    
    # Initialize the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()  # Maximize the window
    
    try:
        driver.get("https://saucedemo.com")
        
        # Wait for the login page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@data-test='username']")))
        
        # Enter username
        time.sleep(3)
        username_field = driver.find_element(By.XPATH, "//input[@data-test='username']")
        username_field.send_keys("standard_user")
        
        # Enter password
        time.sleep(3)
        password_field = driver.find_element(By.XPATH, "//input[@data-test='password']")
        password_field.send_keys("secret_sauce")
        
        # Click on login button
        time.sleep(3)
        login_button = driver.find_element(By.XPATH, "//input[@data-test='login-button']")
        login_button.click()
        
        # Wait for product listing page
        WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))

        # Add Sauce Labs Backpack to cart
        time.sleep(3)
        add_to_cart_button = driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']")
        add_to_cart_button.click()
        
        # Go to the cart page
        time.sleep(3)
        cart_icon = driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']")
        cart_icon.click()
        
        # Validate cart page title
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@data-test='title'][text()='Your Cart']")))
        your_cart_title = driver.find_element(By.XPATH, "//span[@data-test='title']").text
        assert compare_sentences(your_cart_title, "Your Cart")
        
        # Checkout
        time.sleep(3)
        checkout_button = driver.find_element(By.XPATH, "//button[@data-test='checkout']")
        checkout_button.click()
        
        # Wait for checkout step one page
        WebDriverWait(driver, 10).until(EC.url_contains("/checkout-step-one.html"))
        
        # Enter first name
        time.sleep(3)
        first_name_field = driver.find_element(By.XPATH, "//input[@data-test='firstName']")
        first_name_field.send_keys("John")
        
        # Enter last name
        time.sleep(3)
        last_name_field = driver.find_element(By.XPATH, "//input[@data-test='lastName']")
        last_name_field.send_keys("Doe")
        
        # Enter postal code
        time.sleep(3)
        postal_code_field = driver.find_element(By.XPATH, "//input[@data-test='postalCode']")
        postal_code_field.send_keys("12345")
        
        # Click continue to checkout step two
        time.sleep(3)
        continue_button = driver.find_element(By.XPATH, "//input[@data-test='continue']")
        continue_button.click()
        
        # Wait for checkout step two page
        WebDriverWait(driver, 10).until(EC.url_contains("/checkout-step-two.html"))
        
        # Finish checkout
        time.sleep(3)
        finish_button = driver.find_element(By.XPATH, "//button[@data-test='finish']")
        finish_button.click()
        
        # Validate successful checkout
        WebDriverWait(driver, 10).until(EC.url_contains("/checkout-complete.html"))
        complete_order_message = driver.find_element(By.XPATH, "//h2[@data-test='complete-header']").text
        
        if not compare_sentences(complete_order_message, "Thank you for your order!"):
            raise AssertionError("Order completion message did not match!")
        
        print("Test passed successfully.")
        sys.exit(0)

    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)

    finally:
        driver.quit()

test_checkout_process()
