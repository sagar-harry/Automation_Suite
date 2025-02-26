
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        time.sleep(3)
        username_field = self.driver.find_element(By.XPATH, '//*[@id="user-name"]')
        password_field = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')

        username_field.send_keys(username)
        password_field.send_keys(password)
        time.sleep(3)
        login_button.click()

def test_ui():
    try:
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_argument("--incognito")
        options.add_argument("--disable-features=NetworkService")

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get("https://saucedemo.com/")
        time.sleep(3)

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        time.sleep(3)
        bike_light = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')
        bike_light.click()
        time.sleep(3)
        fleece_jacket.click()
        time.sleep(3)

        cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert cart_count.text == '2', "Cart count is not 2"

        time.sleep(3)
        remove_bike_light = driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]')
        remove_fleece_jacket = driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]')
        remove_bike_light.click()
        time.sleep(3)
        remove_fleece_jacket.click()
        time.sleep(3)

        # Verify that cart count element shouldn't exist
        if driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span'):
            raise AssertionError("Cart count element still exists after items are removed")

        time.sleep(3)
        add_bolt_tshirt = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        add_bolt_tshirt.click()
        time.sleep(3)

        cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert cart_count.text == '1', "Cart count is not 1 after adding Bolt T-Shirt"

        driver.quit()
        sys.exit(0)

    except Exception as e:
        print(f"Test failed: {e}")
        driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    test_ui()
