
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

class LoginPage:
    def login(self, driver, username, password):
        driver.get('https://saucedemo.com/')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]')))
        driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

def main():
    options = Options()
    options.headless = True
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-features=NetworkService")
    
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.maximize_window()
        
        login_page = LoginPage()
        login_page.login(driver, 'standard_user', 'secret_sauce')
        
        time.sleep(5)
        
        # Add 'Bike Light' to the cart
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)
        
        # Add 'Fleece Jacket' to the cart
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)

        # Verify the cart badge displays '2'
        cart_count_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        assert cart_count_element.text == '2', "Cart count should be '2'"
        
        # Reset the cart
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@class="cart_button"]')))
        driver.find_elements(By.XPATH, '//*[@class="cart_button"]').click()
        time.sleep(3)
        
        # Verify the cart is empty
        cart_count_elements = driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert len(cart_count_elements) == 0, "Cart should be empty"

        # Add 'Bolt T-Shirt' to the cart after reset
        driver.get('https://saucedemo.com/inventory.html')
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)

        # Verify the cart badge displays '1'
        cart_count_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        assert cart_count_element.text == '1', "Cart count should be '1'"
        
        sys.exit(0)
        
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
        
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
