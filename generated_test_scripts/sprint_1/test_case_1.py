
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run_test():
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-features=NetworkService")

        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://saucedemo.com/')
        time.sleep(5)
        driver.maximize_window()

        login(driver)
        
        time.sleep(3)
        # Add 'Bike Light' to the cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()

        time.sleep(3)
        # Add 'Fleece Jacket' to the cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]'))).click()

        time.sleep(3)
        # Verify cart badge is '2'
        cart_count = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))).text
        assert cart_count == '2', 'Cart badge does not show 2'

        time.sleep(3)
        # Remove 'Bike Light'
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]'))).click()

        time.sleep(3)
        # Remove 'Fleece Jacket'
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]'))).click()

        time.sleep(3)
        # Verify cart count element does not exist
        try:
            driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
            assert False, 'Cart count element still exists'
        except NoSuchElementException:
            pass
        
        time.sleep(3)
        # Add 'Bolt T-Shirt' to the cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()

        time.sleep(3)
        # Verify cart badge is '1'
        cart_count = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))).text
        assert cart_count == '1', 'Cart badge does not show 1'

        driver.save_screenshot("C:/Users/Administrator/Desktop/QE_COE/automated_pipeline_2/captured_screenshots/screenshot.png")

        driver.quit()
        sys.exit(0)
        
    except Exception as e:
        print(f"Test failed: {e}")
        driver.quit()
        sys.exit(1)

def login(driver):
    # Login using LoginPage class method
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="user-name"]'))).send_keys("standard_user")
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]'))).send_keys("secret_sauce")
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]'))).click()

if __name__ == '__main__':
    run_test()
