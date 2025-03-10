
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
        self.username = "//*[@id='user-name']"
        self.password = "//*[@id='password']"
        self.login_button = "//*[@id='login-button']"

    def login(self, user, pwd):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.username))).send_keys(user)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.password))).send_keys(pwd)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.login_button))).click()

def run_test():
    try:
        # Setup Chrome options
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_argument("--incognito")
        options.add_argument("--disable-features=NetworkService")
        
        driver = webdriver.Chrome(options=options)
        
        # Open the website
        driver.get("https://saucedemo.com/")
        time.sleep(5)  # Wait for the page to open
        driver.maximize_window()

        # Initialize and use the LoginPage class
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        time.sleep(3)

        # Add 'Bike Light' to cart
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']"))).click()
        time.sleep(3)

        # Add 'Fleece Jacket' to cart
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']"))).click()
        time.sleep(3)

        # Verify cart badge displays '2'
        cart_badge_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='shopping_cart_container']/a/span")))
        cart_badge_count = cart_badge_element.text
        assert cart_badge_count == '2', f"Cart count was {cart_badge_count}, but expected '2'"

        # Save a screenshot
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")

        sys.exit(0)

    except Exception as e:
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\failed_screenshot.png")
        sys.exit(1)

    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    run_test()
