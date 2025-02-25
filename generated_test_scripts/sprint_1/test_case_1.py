
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
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

def main():
    try:
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument('--incognito')
        chrome_options.add_argument("--disable-features=NetworkService")
        driver = webdriver.Chrome(options=chrome_options)

        driver.get('https://saucedemo.com/')
        time.sleep(5)
        driver.maximize_window()

        # Login
        login_page = LoginPage(driver)
        login_page.login('standard_user', 'secret_sauce')
        time.sleep(3)

        # Add Bike Light to cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
            '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
        time.sleep(3)

        # Add Fleece Jacket to cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
            '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
        time.sleep(3)

        # Verify cart badge shows '2'
        cart_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
            '//*[@id="shopping_cart_container"]/a/span')))
        assert cart_count.text == '2', "Cart does not display 2 items."

        # Reset Cart
        driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[2]/a').click()
        time.sleep(3)
        
        # Come back to the shopping screen
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
            '//*[@id="continue-shopping"]'))).click()
        time.sleep(3)

        # Add Bolt T-Shirt to cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
            '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
        time.sleep(3)

        # Verify cart badge shows '1'
        cart_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
            '//*[@id="shopping_cart_container"]/a/span')))
        assert cart_count.text == '1', "Cart does not display 1 item."

        driver.quit()
        sys.exit(0)

    except Exception as e:
        driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    main()
