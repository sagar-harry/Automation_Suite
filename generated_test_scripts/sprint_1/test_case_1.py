
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

def test_ui_scenario():
    try:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-notifications')
        options.add_argument('--incognito')
        driver = webdriver.Chrome(options=options)

        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        
        bike_light_button = '//*[@id="add-to-cart-sauce-labs-bike-light"]'
        fleece_jacket_button = '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]'
        cart_count = '//*[@id="shopping_cart_container"]/a/span'
        
        # Add Bike Light
        driver.find_element(By.XPATH, bike_light_button).click()
        time.sleep(3)
        
        # Add Fleece Jacket
        driver.find_element(By.XPATH, fleece_jacket_button).click()
        time.sleep(3)

        # Assert cart count
        cart_badge = driver.find_element(By.XPATH, cart_count)
        assert cart_badge.text == '2', 'Cart count should be 2 after adding two items'
        
        # Reset cart
        driver.find_element(By.XPATH, bike_light_button).click()
        time.sleep(3)
        driver.find_element(By.XPATH, fleece_jacket_button).click()
        time.sleep(3)

        # Assert cart is empty
        assert not driver.find_elements(By.XPATH, cart_count), 'Cart should be empty'

        # Add Bolt T-Shirt
        bolt_tshirt_button = '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'
        driver.find_element(By.XPATH, bolt_tshirt_button).click()
        time.sleep(3)

        # Assert cart count
        cart_badge = driver.find_element(By.XPATH, cart_count)
        assert cart_badge.text == '1', 'Cart count should be 1 after adding one item'
        
        driver.quit()
        exit(0)

    except Exception as e:
        print(f'Test failed: {e}')
        driver.quit()
        exit(1)

test_ui_scenario()
