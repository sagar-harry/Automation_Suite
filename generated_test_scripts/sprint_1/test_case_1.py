
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Test Case for Cart Functionality

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

try:
    url = "https://saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"

    # Chrome options
    options = Options()
    options.headless = True
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")
    
    # Initialize WebDriver
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(5)  # Wait for page to load
    driver.maximize_window()

    # Initialize LoginPage and login
    login_page = LoginPage(driver)
    login_page.login(username, password)

    time.sleep(3)

    # Add Bike Light to Cart
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
    time.sleep(3)

    # Add Fleece Jacket to Cart
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]'))).click()
    time.sleep(3)

    # Assert Cart Badge displays '2'
    cart_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))).text
    assert cart_count == '2', "Cart badge count does not match expected '2'"

    # Remove Bike Light from Cart
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]'))).click()
    time.sleep(3)

    # Remove Fleece Jacket from Cart
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]'))).click()
    time.sleep(3)

    # Assert Cart Count Element does not exist
    cart_count_elements = driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    assert not cart_count_elements, "Cart count element still exists when it shouldn't"

    # Add Bolt T-Shirt to Cart
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
    time.sleep(3)

    # Assert Cart Badge displays '1'
    cart_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))).text
    assert cart_count == '1', "Cart badge count does not match expected '1'"

    driver.quit()
    sys.exit(0) # Exit with code 0 indicating the test case passed

except Exception as e:
    print(f"Test case failed: {e}")
    driver.quit()
    sys.exit(1)  # Exit with code 1 indicating the test case failed
