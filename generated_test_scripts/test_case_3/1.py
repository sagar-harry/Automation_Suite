
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
from compare_sentences import compare_sentences

def main():
    
    # Setup Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    
    # Initialize the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    
    try:
        # Step 1: Navigate to the SauceDemo login page
        driver.get("https://www.saucedemo.com/")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='user-name']")))
        time.sleep(3)
        
        # Step 2: Enter username
        username_input = driver.find_element(By.XPATH, "//input[@id='user-name']")
        username_input.send_keys("standard_user")
        time.sleep(3)
        
        # Step 3: Enter password
        password_input = driver.find_element(By.XPATH, "//input[@id='password']")
        password_input.send_keys("secret_sauce")
        time.sleep(3)
        
        # Step 4: Click the Login button
        login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
        login_button.click()
        WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))
        time.sleep(3)
        
        # Step 5: Verify we are on the Product Listing Page
        expected_url = "https://www.saucedemo.com/inventory.html"
        assert driver.current_url == expected_url
        
        # Step 6: Add Sauce Labs Backpack to cart
        add_to_cart_button = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
        add_to_cart_button.click()
        time.sleep(3)
        
        # Step 7: Go to shopping cart
        cart_icon = driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a")
        cart_icon.click()
        WebDriverWait(driver, 10).until(EC.url_contains("/cart.html"))
        time.sleep(3)
        
        # Step 8: Click the Checkout button
        checkout_button = driver.find_element(By.XPATH, "//button[@id='checkout']")
        checkout_button.click()
        WebDriverWait(driver, 10).until(EC.url_contains("/checkout-step-one.html"))
        time.sleep(3)
        
        # Step 9: Fill in checkout information and click Continue
        first_name_input = driver.find_element(By.XPATH, "//input[@id='first-name']")
        first_name_input.send_keys("Tester")
        last_name_input = driver.find_element(By.XPATH, "//input[@id='last-name']")
        last_name_input.send_keys("QA")
        zip_code_input = driver.find_element(By.XPATH, "//input[@id='postal-code']")
        zip_code_input.send_keys("12345")
        continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
        continue_button.click()
        WebDriverWait(driver, 10).until(EC.url_contains("/checkout-step-two.html"))
        time.sleep(3)
        
        # Step 10: Verify order summary includes correct details
        item_name = driver.find_element(By.XPATH, "//div[@data-test='inventory-item-name' and text()='Sauce Labs Backpack']")
        item_price = driver.find_element(By.XPATH, "//div[@data-test='inventory-item-price' and text()='$29.99']")
        assert item_name.is_displayed() and item_price.is_displayed()
        
        # Step 11: Click the Finish button
        finish_button = driver.find_element(By.XPATH, "//button[@id='finish']")
        finish_button.click()
        WebDriverWait(driver, 10).until(EC.url_contains("/checkout-complete.html"))
        time.sleep(3)
        
        # Step 12: Verify order confirmation message
        thank_you_message = driver.find_element(By.XPATH, "//h2[@class='complete-header' and text()='Thank you for your order!']")
        assert thank_you_message.is_displayed()
        
        # Exit with success
        driver.quit()
        sys.exit(0)
    
    except Exception as e:
        print(f"Test failed: {e}")
        driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    main()
