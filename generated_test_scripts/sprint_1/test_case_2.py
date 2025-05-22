
from selenium import webdriver
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
        user_name_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]')))
        password_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]')))
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]')))

        user_name_field.send_keys(username)
        time.sleep(3)
        password_field.send_keys(password)
        time.sleep(3)
        login_button.click()
        time.sleep(3)

def execute_test():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)

    try:
        # Navigate to the website
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        # Add 'Bike Light' and 'Fleece Jacket' to the cart
        bike_light_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        fleece_jacket_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
        
        bike_light_button.click()
        time.sleep(3)
        fleece_jacket_button.click()
        time.sleep(3)

        # Proceed to checkout
        cart_icon = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]/a')))
        cart_icon.click()
        time.sleep(3)

        checkout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout"]')))
        checkout_button.click()
        time.sleep(3)

        # Enter checkout details
        first_name_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]')))
        last_name_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="last-name"]')))
        zip_code_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="postal-code"]')))
        
        first_name_field.send_keys("Jonnathan")
        time.sleep(3)
        last_name_field.send_keys("K")
        time.sleep(3)
        zip_code_field.send_keys("10007")
        time.sleep(3)

        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="continue"]')))
        continue_button.click()
        time.sleep(3)

        # Verify Payment Information label is visible
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]')))

        # Take snapshot of the page
        os.makedirs("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots", exist_ok=True)
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")

        # Test case passed
        sys.exit(0)

    except Exception as e:
        # Take snapshot on failure
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot_fail.png")
        # Test case failed
        sys.exit(1)

    finally:
        driver.quit()

execute_test()
