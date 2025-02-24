
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
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))).send_keys(username)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys(password)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]'))).click()

def test_cart_count():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)
    driver.get("https://saucedemo.com/")
    
    # Wait for page to open and maximize window
    time.sleep(5)
    driver.maximize_window()

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    time.sleep(3)
    
    # Add Bike Light to cart
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
    time.sleep(3)

    # Add Fleece Jacket to cart
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
    time.sleep(3)

    # Verify the cart badge displays '2'
    cart_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
    if cart_count.text == '2':
        print("Test Passed: Cart badge displays '2'")
        driver.quit()
        sys.exit(0)
    else:
        print("Test Failed: Cart badge does not display '2'")
        driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    test_cart_count()
