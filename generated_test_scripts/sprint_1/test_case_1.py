
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

def main():
    options = Options()
    options.headless = True
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")

    try:
        driver = webdriver.Chrome(options=options)
        driver.get("https://saucedemo.com/")
        
        time.sleep(5)
        driver.maximize_window()

        # Perform login
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        # Add items to the cart
        time.sleep(3)
        bike_light = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        bike_light.click()

        time.sleep(3)
        fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')
        fleece_jacket.click()

        time.sleep(3)
        cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert cart_count.text == '2', "Cart count should be 2"

        # Remove items
        time.sleep(3)
        remove_bike_light = driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]')
        remove_bike_light.click()

        time.sleep(3)
        remove_fleece_jacket = driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]')
        remove_fleece_jacket.click()

        time.sleep(3)
        cart_count_not_exist = driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert len(cart_count_not_exist) == 0, "Cart count element should not exist"

        # Add another item
        time.sleep(3)
        add_bolt_tshirt = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        add_bolt_tshirt.click()

        time.sleep(3)
        cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert cart_count.text == '1', "Cart count should be 1"

        driver.quit()
        sys.exit(0)
    except Exception as e:
        print(e)
        sys.exit(1)

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        time.sleep(3)
        username_input = self.driver.find_element(By.XPATH, '//*[@id="user-name"]')
        username_input.send_keys(username)

        time.sleep(3)
        password_input = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        password_input.send_keys(password)

        time.sleep(3)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')
        login_button.click()

if __name__ == "__main__":
    main()
