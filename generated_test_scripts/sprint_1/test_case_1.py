
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def login(driver, username, password):
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

def main():
    try:
        # Set up Chrome options for headless, incognito, disable notifications
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-notifications")

        # Start Chrome browser with options
        driver = webdriver.Chrome(options=chrome_options)

        # Maximize window
        driver.maximize_window()

        # Open the URL
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        # Log in
        login(driver, "standard_user", "secret_sauce")
        time.sleep(3)

        # Add 'Bike Light' to the cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
        time.sleep(3)

        # Add 'Fleece Jacket' to the cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
        time.sleep(3)

        # Verify cart badge count is '2'
        cart_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))).text
        assert cart_count == '2', f"Expected cart count: 2, Got: {cart_count}"
        time.sleep(3)

        # Remove all items from the cart (reset cart)
        driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)

        # Verify the cart is empty
        cart_badge = driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert len(cart_badge) == 0, "Expected cart to be empty"
        time.sleep(3)

        # Add 'Bolt T-Shirt' after reset
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
        time.sleep(3)

        # Verify cart badge count is '1'
        cart_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))).text
        assert cart_count == '1', f"Expected cart count: 1, Got: {cart_count}"

        # Exit with code 0 (success)
        driver.quit()
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
        # Exit with code 1 (failure)
        if 'driver' in locals():
            driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    main()
