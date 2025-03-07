
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from compare_sentences import compare_sentences

def main():
    try:
        # Chrome Options
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--incognito")

        # Initialize WebDriver
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()

        # Open 'SauceDemo' login page
        driver.get("https://www.saucedemo.com")
        time.sleep(3)  # Wait for 3 seconds before each action

        # Enter Username
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@data-test='username']"))
        )
        username_field.send_keys("standard_user")
        time.sleep(3)

        # Enter Password
        password_field = driver.find_element(By.XPATH, "//input[@data-test='password']")
        password_field.send_keys("secret_sauce")
        time.sleep(3)
        
        # Click Login button
        login_button = driver.find_element(By.XPATH, "//input[@data-test='login-button']")
        login_button.click()
        time.sleep(3)

        # Validate redirection to Product Listing Page
        product_listing_page_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@data-test='title' and text()='Products']"))
        )
        assert compare_sentences(product_listing_page_title.text, "Products")
        
        # Add a product to the cart
        add_to_cart_button = driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']")
        add_to_cart_button.click()
        time.sleep(3)

        # Click on the cart icon
        cart_icon = driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']")
        cart_icon.click()
        time.sleep(3)

        # Validate redirection to Shopping Cart Page
        shopping_cart_page_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@data-test='title' and text()='Your Cart']"))
        )
        assert compare_sentences(shopping_cart_page_title.text, "Your Cart")

        # Click on Checkout
        checkout_button = driver.find_element(By.XPATH, "//button[@data-test='checkout']")
        checkout_button.click()
        time.sleep(3)

        # Validate redirection to Checkout Step 1: User Info Page
        checkout_step_1_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@data-test='title' and text()='Checkout: Your Information']"))
        )
        assert compare_sentences(checkout_step_1_title.text, "Checkout: Your Information")
        
        # Enter User Info
        first_name_field = driver.find_element(By.XPATH, "//input[@data-test='firstName']")
        first_name_field.send_keys("John")
        time.sleep(3)

        last_name_field = driver.find_element(By.XPATH, "//input[@data-test='lastName']")
        last_name_field.send_keys("Doe")
        time.sleep(3)

        zip_code_field = driver.find_element(By.XPATH, "//input[@data-test='postalCode']")
        zip_code_field.send_keys("90210")
        time.sleep(3)

        # Click Continue
        continue_button = driver.find_element(By.XPATH, "//input[@data-test='continue']")
        continue_button.click()
        time.sleep(3)

        # Validate redirection to Checkout Step 2: Order Overview page
        checkout_step_2_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@data-test='title' and text()='Checkout: Overview']"))
        )
        assert compare_sentences(checkout_step_2_title.text, "Checkout: Overview")

        # Click Finish
        finish_button = driver.find_element(By.XPATH, "//button[@data-test='finish']")
        finish_button.click()
        time.sleep(3)

        # Validate redirection to Order Confirmation Page and the thank you message
        order_confirmation_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@data-test='title' and text()='Checkout: Complete!']"))
        )
        assert compare_sentences(order_confirmation_title.text, "Checkout: Complete!")

        thank_you_message = driver.find_element(By.XPATH, "//h2[@data-test='complete-header' and text()='Thank you for your order!']")
        assert compare_sentences(thank_you_message.text, "Thank you for your order!")

        # Exit with success
        sys.exit(0)
    except Exception as e:
        print(f"Test failed: {e}")
        # Exit with failure
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
