
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import os

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(username)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()

def run_test():
    try:
        # Chrome options
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_argument("--incognito")
        options.add_argument("--disable-features=NetworkService")

        # Set up Chrome driver
        driver = webdriver.Chrome(options=options)
        
        # Open the website
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()
        
        # Login
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        time.sleep(3)

        # Wait and add 'Bike Light' to cart
        bike_light_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))
        )
        bike_light_button.click()
        time.sleep(3)

        # Wait and add 'Fleece Jacket' to cart
        fleece_jacket_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"))
        )
        fleece_jacket_button.click()
        time.sleep(3)

        # Verify the cart badge
        cart_badge = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']"))
        )
        assert cart_badge.text == '2', f"Expected cart badge count '2', but got '{cart_badge.text}'"

        # Save a screenshot
        screenshot_path = "C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png"
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        driver.save_screenshot(screenshot_path)

        # Close driver
        driver.quit()

        # Successful test case
        sys.exit(0)

    except Exception as e:
        print(f"Test failed: {e}")
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error_screenshot.png")
        driver.quit()
        sys.exit(1)

run_test()
