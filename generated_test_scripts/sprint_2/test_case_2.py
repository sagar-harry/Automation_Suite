
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

def save_snapshot(driver):
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = '//*[@id="user-name"]'
        self.password_input = '//*[@id="password"]'
        self.login_button = '//*[@id="login-button"]'

    def login(self, username, password):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.username_input)))
        self.driver.find_element(By.XPATH, self.username_input).send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.password_input).send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.login_button).click()

def test_cart_count():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://saucedemo.com/')
    driver.maximize_window()
    time.sleep(5)
    
    # Login
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    time.sleep(3)

    try:
        # Add 'Bike Light' to the cart
        bike_light_button = '//*[@id="add-to-cart-sauce-labs-bike-light"]'
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, bike_light_button)))
        driver.find_element(By.XPATH, bike_light_button).click()
        time.sleep(3)

        # Add 'Fleece Jacket' to the cart
        fleece_jacket_button = '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, fleece_jacket_button)))
        driver.find_element(By.XPATH, fleece_jacket_button).click()
        time.sleep(3)

        # Verify cart count
        cart_count_xpath = '//*[@id="shopping_cart_container"]/a/span'
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, cart_count_xpath)))
        cart_count = driver.find_element(By.XPATH, cart_count_xpath).text

        if cart_count != '2':
            save_snapshot(driver)
            raise Exception("Cart count is incorrect. Expected '2', but got '{}'.".format(cart_count))

        print("Test passed.")
        sys.exit(0)

    except Exception as e:
        print(f"Test failed: {e}")
        save_snapshot(driver)
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    test_cart_count()
