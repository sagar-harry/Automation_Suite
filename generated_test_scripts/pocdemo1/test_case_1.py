
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import sys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_field = self.driver.find_element(By.XPATH, "//*[@id='user-name']")
        password_field = self.driver.find_element(By.XPATH, "//*[@id='password']")
        login_button = self.driver.find_element(By.XPATH, "//*[@id='login-button']")
        
        username_field.send_keys(username)
        time.sleep(3)
        password_field.send_keys(password)
        time.sleep(3)
        login_button.click()
        
def test_purchase_flow():
    # Chrome options
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")
    
    # Initialize WebDriver
    driver = webdriver.Chrome(options=options)
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    
    # Maximize window
    driver.maximize_window()

    try:
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        # Add items to cart
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']"))
        ).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']"))
        ).click()
        time.sleep(3)

        # Go to cart
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='shopping_cart_container']/a"))
        ).click()
        time.sleep(3)

        # Proceed to checkout
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='checkout']"))
        ).click()
        time.sleep(3)

        # Enter user information and continue
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='first-name']"))
        ).send_keys("somename")
        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='last-name']"))
        ).send_keys("lastname")
        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='postal-code']"))
        ).send_keys("123456")
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='continue']"))
        ).click()
        time.sleep(3)

        # Complete the purchase
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='finish']"))
        ).click()
        time.sleep(3)

        # Go back to products
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='back-to-products']"))
        ).click()
        time.sleep(3)

        # Logout
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='react-burger-menu-btn']"))
        ).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='logout_sidebar_link']"))
        ).click()
        time.sleep(3)

        sys.exit(0)

    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    test_purchase_flow()
