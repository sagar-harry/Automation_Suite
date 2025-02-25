
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        user_name_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]')))
        password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]')))
        login_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="login-button"]')))
       
        user_name_input.send_keys(username)
        time.sleep(3)
        password_input.send_keys(password)
        time.sleep(3)
        login_button.click()
        time.sleep(3)

def test_ui_scenario():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")
    
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()
        time.sleep(3)

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        # Add 'Bike Light' to the cart
        bike_light_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        bike_light_button.click()
        time.sleep(3)

        # Add 'Fleece Jacket' to the cart
        fleece_jacket_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')))
        fleece_jacket_button.click()
        time.sleep(3)

        # Verify cart badge displays '2'
        cart_badge = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        assert cart_badge.text == '2', "Cart badge count is incorrect"
        
        # Remove 'Bike Light'
        remove_bike_light_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]')))
        remove_bike_light_button.click()
        time.sleep(3)

        # Remove 'Fleece Jacket'
        remove_fleece_jacket_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]')))
        remove_fleece_jacket_button.click()
        time.sleep(3)

        # Verify cart count element doesn't exist
        try:
            driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
            cart_badge_exists = True
        except:
            cart_badge_exists = False
        
        assert not cart_badge_exists, "Cart badge element exists when it should not"

        # Add 'Bolt T-Shirt' to the cart
        bolt_tshirt_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
        bolt_tshirt_button.click()
        time.sleep(3)

        # Verify cart badge displays '1'
        cart_badge = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        assert cart_badge.text == '1', "Cart badge count is incorrect after adding Bolt T-Shirt"

        # Close browser and pass the test
        driver.quit()
        sys.exit(0)
    
    except Exception as e:
        print(e)
        driver.quit()
        sys.exit(1)

test_ui_scenario()
