
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        user_field = self.driver.find_element(By.XPATH, '//*[@id="user-name"]')
        user_field.send_keys(username)
        pass_field = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        pass_field.send_keys(password)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')
        login_button.click()

def main():
    options = Options()
    options.headless = True
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        time.sleep(3)

        bike_light_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        bike_light_button.click()
        time.sleep(3)

        fleece_jacket_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
        fleece_jacket_button.click()
        time.sleep(3)

        cart_count = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        
        assert cart_count.text == '2', "Cart count should be '2' after adding two items"

        # Reset Cart
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]').click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//button[contains(text(),"Remove")]'))).click()
        time.sleep(3)
        cart_count = driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        
        assert len(cart_count) == 0, "Cart should be empty after reset"

        # Add Bolt T-Shirt after reset
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        login_page.login("standard_user", "secret_sauce")
        time.sleep(3)

        bolt_tshirt_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
        bolt_tshirt_button.click()
        time.sleep(3)

        cart_count = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        
        assert cart_count.text == '1', "Cart count should be '1' after adding Bolt T-Shirt"

        exit(0)
    except Exception as e:
        print(f"Test failed with exception: {e}")
        exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
