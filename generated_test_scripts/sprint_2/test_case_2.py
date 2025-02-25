
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]')))
        password_field = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')

        time.sleep(3)
        username_field.send_keys(username)
        password_field.send_keys(password)

        time.sleep(3)
        login_button.click()

def test_add_to_cart():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--incognito')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-features=NetworkService')
    options.add_argument("--start-maximized")

    with webdriver.Chrome(options=options) as driver:
        driver.get('https://saucedemo.com/')
        time.sleep(5)

        login_page = LoginPage(driver)
        login_page.login('standard_user', 'secret_sauce')

        # Add Bike Light to the cart
        bike_light_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        time.sleep(3)
        bike_light_button.click()

        # Add Fleece Jacket to the cart
        fleece_jacket_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
        time.sleep(3)
        fleece_jacket_button.click()

        # Verify the cart badge displays '2'
        cart_count = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        time.sleep(3)
        if cart_count.text == '2':
            print('Test Passed: Cart badge displays 2')
            sys.exit(0)
        else:
            print('Test Failed: Cart badge is not displaying 2')
            sys.exit(1)

if __name__ == "__main__":
    try:
        test_add_to_cart()
    except Exception as e:
        print("Test Failed with exception:", e)
        sys.exit(1)
