
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

def setUp():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")
    
    driver = webdriver.Chrome(options=options)
    driver.get("https://saucedemo.com/")
    driver.maximize_window()
    time.sleep(5)
    return driver

def wait_and_click(driver, locator):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, locator))).click()
    time.sleep(3)

def wait_for_element(driver, locator):
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, locator)))
    time.sleep(3)
    return element

def login(driver):
    wait_for_element(driver, '//*[@id="user-name"]').send_keys("standard_user")
    wait_for_element(driver, '//*[@id="password"]').send_keys("secret_sauce")
    wait_and_click(driver, '//*[@id="login-button"]')

def run_test():
    driver = setUp()
    try:
        login(driver)

        # Add 'Bike Light' and 'Fleece Jacket' to the cart
        wait_and_click(driver, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        wait_and_click(driver, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')

        # Verify cart badge is '2'
        cart_badge = wait_for_element(driver, '//*[@id="shopping_cart_container"]/a/span')
        assert cart_badge.text == '2', "Cart badge did not display expected value '2'"

        # Reset (remove products from cart)
        driver.get('https://saucedemo.com/cart.html')
        wait_and_click(driver, '//*[@id="remove-sauce-labs-bike-light"]')
        wait_and_click(driver, '//*[@id="remove-sauce-labs-bolt-t-shirt"]')

        # Verify cart is empty
        driver.get('https://saucedemo.com/')
        assert not cart_badge.is_displayed(), "Cart is not empty when it should be"

        # Add 'Bolt T-Shirt' to the cart
        wait_and_click(driver, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')

        # Verify cart badge is '1'
        cart_badge = wait_for_element(driver, '//*[@id="shopping_cart_container"]/a/span')
        assert cart_badge.text == '1', "Cart badge did not display expected value '1'"

        sys.exit(0)

    except AssertionError as e:
        print(str(e))
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    run_test()
