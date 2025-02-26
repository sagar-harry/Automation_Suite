
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

# Initialize the Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--disable-notifications")
options.add_argument("--disable-features=NetworkService")

# Test constants
URL = "https://saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

try:
    # Start the browser
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(URL)
    time.sleep(5)  # Wait for page to load

    # Login
    class LoginPage:
        @staticmethod
        def login(driver, username, password):
            wait = WebDriverWait(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))).send_keys(username)
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys(password)
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-button"]'))).click()
            time.sleep(3)

    # Perform login
    LoginPage.login(driver, USERNAME, PASSWORD)

    # Add Bike Light to cart
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
    time.sleep(3)

    # Add Fleece Jacket to cart
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]'))).click()
    time.sleep(3)

    # Verify cart badge displays 2
    cart_count = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
    assert cart_count.text == '2', "Cart badge did not show 2"

    # Remove Bike Light
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]'))).click()
    time.sleep(3)

    # Remove Fleece Jacket
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]'))).click()
    time.sleep(3)

    # Verify cart count element doesn't exist
    cart_badge_element = driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    assert len(cart_badge_element) == 0, "Cart count element should not exist"

    # Add Bolt T-Shirt to cart
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
    time.sleep(3)

    # Verify cart badge displays 1
    cart_count = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
    assert cart_count.text == '1', "Cart badge did not show 1"

    sys.exit(0)  # Exit with success

except Exception as e:
    print(f"Test failed: {e}")
    sys.exit(1)  # Exit with failure

finally:
    driver.quit()
