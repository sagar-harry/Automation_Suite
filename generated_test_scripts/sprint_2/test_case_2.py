
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.XPATH, '//*[@id="user-name"]')
        self.password_input = (By.XPATH, '//*[@id="password"]')
        self.login_button = (By.XPATH, '//*[@id="login-button"]')

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.username_input)).send_keys(username)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password_input)).send_keys(password)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button)).click()

def test_add_items_to_cart():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')
        options.add_argument('--disable-notifications')
        options.add_argument('--disable-popups')
        options.add_argument('--disable-features=NetworkService')

        driver = webdriver.Chrome(options=options)
        driver.get('https://saucedemo.com/')
        driver.maximize_window()
        time.sleep(5)
        
        login_page = LoginPage(driver)
        login_page.login('standard_user', 'secret_sauce')

        bike_light = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        fleece_jacket = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        cart_count = (By.XPATH, '//*[@id="shopping_cart_container"]/a/span')

        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(bike_light)).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(fleece_jacket)).click()

        time.sleep(3)
        cart_count_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(cart_count)).text
        
        assert cart_count_text == '2', "Cart count did not match expected value"
        
        driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\cart_test_passed.png')
        sys.exit(0)

    except Exception as e:
        driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\cart_test_failed.png')
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    test_add_items_to_cart()
