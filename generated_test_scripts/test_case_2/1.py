
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time
from compare_sentences import compare_sentences

def test_add_to_cart():
    # Chrome options
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    
    url = "https://saucedemo.com"
    try:
        # 1. Navigate to the login page
        driver.get(url)
        time.sleep(3)  # Wait for 3 seconds

        # 2. Enter the username
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='user-name']"))
        )
        username_input.send_keys("standard_user")
        time.sleep(3)  # Wait for 3 seconds

        # 3. Enter the password
        password_input = driver.find_element(By.XPATH, "//input[@id='password']")
        password_input.send_keys("secret_sauce")
        time.sleep(3)  # Wait for 3 seconds
        
        # 4. Click on the login button
        login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
        login_button.click()
        time.sleep(3)  # Wait for 3 seconds
        
        # 5. Ensure that we are on the product listing page
        current_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='title']"))
        )
        if not compare_sentences(current_title.text, "Products"):
            raise Exception("Failed to verify product listing page.")
        
        # 6. Click "Add to cart" button for "Sauce Labs Backpack"
        add_to_cart_button = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
        add_to_cart_button.click()
        time.sleep(3)  # Wait for 3 seconds

        # 7. Verify the cart badge displays "1"
        cart_badge = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='shopping_cart_container']//span[@class='shopping_cart_badge']"))
        )
        if not compare_sentences(cart_badge.text, "1"):
            raise Exception("Cart count is not as expected.")
        
        # 8. Click on the cart icon
        cart_icon = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
        cart_icon.click()
        time.sleep(3)  # Wait for 3 seconds
        
        # 9. Verify the shopping cart page title
        cart_page_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='title' and text()='Your Cart']"))
        )
        if not compare_sentences(cart_page_title.text, "Your Cart"):
            raise Exception("Shopping cart page title does not match.")

        print("Test Passed")
        sys.exit(0)

    except Exception as e:
        print(f"Test Failed: {e}")
        sys.exit(1)

    finally:
        driver.quit()

test_add_to_cart()
