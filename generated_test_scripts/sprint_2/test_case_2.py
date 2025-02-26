
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
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]')))
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(3)

def test_add_to_cart():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument('--disable-features=NetworkService')
    options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
    
    driver = webdriver.Chrome(options=options)

    try:
        driver.maximize_window()
        driver.get('https://saucedemo.com/')
        time.sleep(5)

        login_page = LoginPage(driver)
        login_page.login('standard_user', 'secret_sauce')
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text

        assert cart_count == '2', f'Expected cart count to be 2 but got {cart_count}'
        sys.exit(0)
    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)
    finally:
        driver.quit()

test_add_to_cart()
