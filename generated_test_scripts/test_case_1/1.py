
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from compare_sentences import compare_sentences

def main():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=options)
    
    try:
        # Maximize the page
        driver.maximize_window()
        
        # Navigate to the specified URL
        driver.get("https://saucedemo.com")
        
        # Wait for the page to load
        time.sleep(3)
        
        # Locate and fill in the username
        username_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='user-name']")))
        username_input.send_keys("standard_user")
        time.sleep(3)
        
        # Locate and fill in the password
        password_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='password']")))
        password_input.send_keys("secret_sauce")
        time.sleep(3)

        # Locate and click the login button
        login_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='login-button']")))
        login_button.click()
        time.sleep(3)
        
        # Verify if redirected to the product listing page
        expected_title = "Products"
        actual_title_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@class='title']")))
        actual_title = actual_title_element.text

        if not compare_sentences(expected_title, actual_title):
            print("Failed to redirect to product listing page.")
            sys.exit(1)
        
        # Locate and click the 'Add to cart' button for 'Sauce Labs Backpack'
        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")))
        add_to_cart_button.click()
        time.sleep(3)

        # Verify that the product is added to the cart and the cart badge is updated
        cart_badge = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@id='shopping_cart_container']//span[@class='shopping_cart_badge']")))
        
        expected_cart_count = "1"
        actual_cart_count = cart_badge.text

        if not compare_sentences(expected_cart_count, actual_cart_count):
            print("Cart badge did not update correctly.")
            sys.exit(1)
            
        print("Test case passed.")
        sys.exit(0)
        
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
        
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
