
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import sys
import os
import time

def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=NetworkService")
    driver = webdriver.Chrome(options=options)

    try:
        # Open the website
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()

        # Login
        login(driver)

        # Add Bike Light and Fleece Jacket
        add_to_cart(driver, By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        add_to_cart(driver, By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')

        # Assert cart badge
        assert_cart_count(driver, '2')

        # Remove Bike Light and Fleece Jacket
        remove_from_cart(driver, By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]')
        remove_from_cart(driver, By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]')

        # Assert cart count element doesn't exist
        assert_cart_element_absent(driver)

        # Add Bolt T-Shirt
        add_to_cart(driver, By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')

        # Assert cart badge
        assert_cart_count(driver, '1')

        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")
        sys.exit(0)

    except Exception as e:
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error_screenshot.png")
        sys.exit(1)

    finally:
        driver.quit()

def login(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))).send_keys("standard_user")
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(3)

def add_to_cart(driver, by, locator):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, locator))).click()
    time.sleep(3)

def remove_from_cart(driver, by, locator):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, locator))).click()
    time.sleep(3)

def assert_cart_count(driver, count):
    cart_count = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))).text
    assert cart_count == count
    time.sleep(3)

def assert_cart_element_absent(driver):
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        raise AssertionError('Cart count element should not exist')
    except TimeoutException:
        time.sleep(3)

if __name__ == "__main__":
    main()
