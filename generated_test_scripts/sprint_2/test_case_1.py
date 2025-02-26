
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        )
        username_input.send_keys(username)
        
        password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))
        )
        password_input.send_keys(password)
        
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')
        login_button.click()

def main():
    try:
        options = Options()
        options.headless = True
        options.add_argument("--disable-notifications")
        options.add_argument("--incognito")
        options.add_argument("--disable-features=NetworkService")

        driver = webdriver.Chrome(options=options)
        
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        time.sleep(3)

        # Add 'Bike Light' to cart
        bike_light_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        )
        bike_light_button.click()
        time.sleep(3)

        # Add 'Fleece Jacket' to cart
        fleece_jacket_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        )
        fleece_jacket_button.click()
        time.sleep(3)

        # Click on the cart icon
        cart_icon = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a'))
        )
        cart_icon.click()
        time.sleep(3)

        # Proceed to checkout
        checkout_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout"]'))
        )
        checkout_button.click()
        time.sleep(3)

        # Enter checkout details
        first_name = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]'))
        )
        first_name.send_keys("somename")
        
        last_name = driver.find_element(By.XPATH, '//*[@id="last-name"]')
        last_name.send_keys("lastname")
        
        postal_code = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
        postal_code.send_keys("123456")
        time.sleep(3)

        # Continue checkout
        continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
        continue_button.click()
        time.sleep(3)

        # Finish purchase
        finish_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="finish"]'))
        )
        finish_button.click()
        time.sleep(3)

        # Return to homepage and logout
        back_to_products = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="back-to-products"]'))
        )
        back_to_products.click()
        time.sleep(3)

        # Open logout sidebar and logout
        logout_sidebar = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="react-burger-menu-btn"]'))
        )
        logout_sidebar.click()
        time.sleep(3)

        logout_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="logout_sidebar_link"]'))
        )
        logout_button.click()
        time.sleep(3)

        driver.quit()
        sys.exit(0)
    
    except Exception as e:
        print(f"Test failed: {e}")
        if driver:
            driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    main()
