
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

# Initialize Chrome options
options = Options()
options.add_argument("--headless")
options.add_argument("--incognito")
options.add_argument('--disable-notifications')
options.add_argument('--disable-popup-blocking')
options.add_argument('--disable-features=NetworkService')

try:
    # Initialize WebDriver
    driver = webdriver.Chrome(options=options)

    # Open the target URL
    driver.get("https://saucedemo.com/")
    time.sleep(5)

    # Maximize the window
    driver.maximize_window()

    # Login Method in LoginPage class
    class LoginPage:
        def __init__(self, driver):
            self.driver = driver

        def login(self, username, password):
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]')))
            username_field = self.driver.find_element(By.XPATH, '//*[@id="user-name"]')
            password_field = self.driver.find_element(By.XPATH, '//*[@id="password"]')
            login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')

            time.sleep(3)
            username_field.send_keys(username)
            time.sleep(3)
            password_field.send_keys(password)
            time.sleep(3)
            login_button.click()

    # Execute login
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # Wait for page transition
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]')))

    # Add 'Bike Light' to cart
    bike_light = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
    time.sleep(3)
    bike_light.click()

    # Add 'Fleece Jacket' to cart
    fleece_jacket = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
    time.sleep(3)
    fleece_jacket.click()

    # Verify cart badge displays '2'
    cart_count_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
    time.sleep(3)
    cart_count = cart_count_element.text

    if cart_count == '2':
        sys.exit(0)
    else:
        sys.exit(1)

except Exception as e:
    sys.exit(1)  # Exit with code 1 in case of any exceptions

finally:
    driver.quit()
