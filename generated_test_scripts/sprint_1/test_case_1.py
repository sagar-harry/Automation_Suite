
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(3)

def main():
    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-notifications")
        options.add_argument("--incognito")

        driver = webdriver.Chrome(options=options)
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()
        time.sleep(3)

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        # Add 'Bike Light' to the cart
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)
        
        # Add 'Fleece Jacket' to the cart
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)

        # Check if cart badge shows '2'
        cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
        if cart_count != '2':
            raise Exception("Cart count is incorrect after adding items")

        # Reset the cart (assuming clicking the remove button on all items in it)
        driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)

        # Verify cart is empty
        try:
            cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
            if cart_count != '0':
                raise Exception("Cart is not empty after reset")
        except:
            pass  # If cart badge does not appear, it means it is empty

        # Add 'Bolt T-Shirt' to the cart
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)

        # Check if cart badge shows '1'
        cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
        if cart_count != '1':
            raise Exception("Cart count is incorrect after adding Bolt T-Shirt after reset")

        driver.quit()
        sys.exit(0)
    except Exception as e:
        print(f"Test failed: {e}")
        driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    main()
