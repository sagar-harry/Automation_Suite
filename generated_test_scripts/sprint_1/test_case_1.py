
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

def wait_for_element(driver, timeout, criteria):
    for _ in range(timeout):
        try:
            element = driver.find_element(*criteria)
            if element:
                return element
        except:
            pass
        time.sleep(1)
    sys.exit(1)

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

def test_ui_scenario():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()
    
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        
        # Add Bike Light to Cart
        bike_light = wait_for_element(driver, 10, (By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        bike_light.click()
        time.sleep(3)

        # Add Fleece Jacket to Cart
        fleece_jacket = wait_for_element(driver, 10, (By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]'))
        fleece_jacket.click()
        time.sleep(3)

        # Check Cart Badge for '2'
        cart_count = wait_for_element(driver, 10, (By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        assert cart_count.text == '2', "Cart count is not 2"
        time.sleep(3)

        # Remove Bike Light
        remove_bike_light = wait_for_element(driver, 10, (By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]'))
        remove_bike_light.click()
        time.sleep(3)

        # Remove Fleece Jacket
        remove_fleece_jacket = wait_for_element(driver, 10, (By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]'))
        remove_fleece_jacket.click()
        time.sleep(3)

        # Check Cart Element Does Not Exist
        try:
            driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
            sys.exit(1)
        except:
            pass

        # Add Bolt T-Shirt to Cart
        bolt_tshirt = wait_for_element(driver, 10, (By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        bolt_tshirt.click()
        time.sleep(3)

        # Check Cart Badge for '1'
        cart_count = wait_for_element(driver, 10, (By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        assert cart_count.text == '1', "Cart count is not 1"
        time.sleep(3)

        sys.exit(0)

    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)
    
    finally:
        driver.quit()

test_ui_scenario()
