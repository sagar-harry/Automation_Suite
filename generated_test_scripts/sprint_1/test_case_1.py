
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def login(driver):
    driver.get("https://saucedemo.com/")
    time.sleep(5)  # Wait after opening the page
    driver.maximize_window()
    time.sleep(3)

    username_field = driver.find_element(By.XPATH, '//*[@id="user-name"]')
    password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
    login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')

    username_field.send_keys("standard_user")
    time.sleep(3)
    password_field.send_keys("secret_sauce")
    time.sleep(3)
    login_button.click()

def test_ui_scenario():
    options = Options()
    options.headless = True
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)

    try:
        login(driver)
        time.sleep(5)

        # Add 'Bike Light' to cart
        bike_light = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        bike_light.click()
        time.sleep(3)

        # Add 'Fleece Jacket' to cart
        fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        fleece_jacket.click()
        time.sleep(3)

        # Verify cart badge shows '2'
        cart_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert cart_badge.text == '2', "Cart badge did not display '2' after adding products"
        time.sleep(3)

        # Reset cart (remove items)
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        time.sleep(3)

        remove_buttons = driver.find_elements(By.CLASS_NAME, 'cart_button')
        for remove_button in remove_buttons:
            remove_button.click()
            time.sleep(3)

        driver.find_element(By.ID, 'continue-shopping').click()
        time.sleep(3)

        # Verify cart is empty
        cart_badge = driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert len(cart_badge) == 0, "Cart is not empty after reset"
        time.sleep(3)

        # Add 'Bolt T-Shirt' to cart after reset
        bolt_tshirt = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        bolt_tshirt.click()
        time.sleep(3)

        # Verify cart badge shows '1'
        cart_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert cart_badge.text == '1', "Cart badge did not display '1' after adding 'Bolt T-Shirt'"
        time.sleep(3)

        driver.quit()
        exit(0)

    except AssertionError as error:
        print(f"Assertion Error: {error}")
        driver.quit()
        exit(1)

if __name__ == "__main__":
    test_ui_scenario()
