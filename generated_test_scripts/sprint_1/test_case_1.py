
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        )
        username_field.send_keys(username)
        time.sleep(3)  # Wait before the next action

        password_field = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        password_field.send_keys(password)
        time.sleep(3)  # Wait before the next action

        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')
        login_button.click()
        time.sleep(3)  # Wait after login

def test_ui_scenario():
    options = Options()
    options.headless = True
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://saucedemo.com/")
        time.sleep(5)  # Wait after page load
        driver.maximize_window()

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        # Add products to cart
        bike_light = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        )
        bike_light.click()
        time.sleep(3)  # Wait before the next action

        fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        fleece_jacket.click()
        time.sleep(3)  # Wait before the next action

        # Verify cart count is 2
        cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
        assert cart_count == '2', f"Expected cart count to be 2, but got {cart_count}"

        # Reset cart
        driver.find_element(By.XPATH, '//*[@class="shopping_cart_link"]').click()  # Navigate to cart
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@class="cart_button"]'))  # Change to correct locator for remove
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@class="cart_button"]'))  # Change to correct locator for remove
        ).click()
        time.sleep(3)  # Wait after reset

        # Verify cart is empty
        cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
        assert cart_count == '', "Expected cart to be empty after reset"

        # Add new product to cart
        driver.back()  # Navigate back to product page
        bolt_tshirt = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        )
        bolt_tshirt.click()
        time.sleep(3)  # Wait before the next action

        # Verify cart count is 1
        cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
        assert cart_count == '1', f"Expected cart count to be 1, but got {cart_count}"

        print("Test passed")
        sys.exit(0)

    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    test_ui_scenario()
