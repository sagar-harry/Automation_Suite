
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import sys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(3)  # wait after login action

def main():
    url = "https://saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"
    
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    
    time.sleep(5)  # wait for 5 seconds after opening the page
    driver.maximize_window()
    time.sleep(3)  # wait after maximizing the page

    # Create login page object and perform login
    login_page = LoginPage(driver)
    login_page.login(username, password)
    
    try:
        # Add 'Bike Light' to the cart
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        ).click()
        time.sleep(3)

        # Add 'Fleece Jacket' to the cart
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        ).click()
        time.sleep(3)

        # Verify cart badge displays '2'
        cart_count = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        ).text
        assert cart_count == '2'

        # Reset the cart
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]'))
        ).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="remove-sauce-labs-bolt-t-shirt"]'))
        ).click()
        time.sleep(3)

        # Verify cart is empty
        driver.back()
        cart_badge = driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert len(cart_badge) == 0

        # Add 'Bolt T-Shirt' to the cart
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        ).click()
        time.sleep(3)

        # Verify cart badge displays '1'
        cart_count = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        ).text
        assert cart_count == '1'

        sys.exit(0)  # Test passed
    except AssertionError:
        sys.exit(1)  # Test failed
    except TimeoutException:
        sys.exit(1)  # Test failed
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
