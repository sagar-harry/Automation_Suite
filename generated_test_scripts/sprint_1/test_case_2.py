
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
        time.sleep(3)  # Wait for 3 secs before action
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        time.sleep(3)  # Wait for 3 secs before action
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(3)  # Wait for 3 secs after action

def test_ui_checkout():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-notifications')
    options.add_argument('--incognito')
    options.add_argument('--disable-features=NetworkService')

    driver = webdriver.Chrome(options=options)
    driver.get("https://saucedemo.com/")
    driver.maximize_window()
    time.sleep(5)  # Wait for 5 secs after opening the page

    # Login
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # Add Bike Light to cart
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    time.sleep(3)  # Wait for 3 secs after action

    # Add Fleece Jacket to cart
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(3)  # Wait for 3 secs after action

    # Go to Cart
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    time.sleep(3)  # Wait for 3 secs after action

    # Proceed to Checkout
    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
    time.sleep(3)  # Wait for 3 secs after action

    # Enter Checkout Information
    driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("somename")
    time.sleep(3)  # Wait for 3 secs after action
    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("lastname")
    time.sleep(3)  # Wait for 3 secs after action
    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("123456")
    time.sleep(3)  # Wait for 3 secs after action
    
    # Continue
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()
    time.sleep(3)  # Wait for 3 secs after action

    # Validate Payment Information visibility
    try:
        payment_info_label = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]')
        if payment_info_label.is_displayed():
            sys.exit(0)  # Test case passed
        else:
            sys.exit(1)  # Test case failed
    except:
        sys.exit(1)  # Test case failed

    driver.quit()

test_ui_checkout()
