
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def main():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--incognito")
        options.add_argument("--disable-features=NetworkService")

        # Initialize WebDriver
        driver = webdriver.Chrome(options=options)

        # Open the website and maximize window
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()

        # Login
        username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]')))
        username_input.send_keys("standard_user")
        time.sleep(3)
        password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
        password_input.send_keys("secret_sauce")
        time.sleep(3)
        login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
        login_button.click()

        # Add 'Bike Light' to cart
        time.sleep(3)
        bike_light_add_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        bike_light_add_btn.click()

        # Add 'Fleece Jacket' to cart
        time.sleep(3)
        fleece_jacket_add_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')))
        fleece_jacket_add_btn.click()

        # Verify cart count is '2'
        time.sleep(3)
        cart_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        assert cart_count.text == '2'

        # Remove bike light
        time.sleep(3)
        bike_light_remove = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]')))
        bike_light_remove.click()

        # Remove fleece jacket
        time.sleep(3)
        fleece_jacket_remove = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]')))
        fleece_jacket_remove.click()

        # Verify cart count element doesn't exist
        time.sleep(3)
        assert not driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')

        # Add 'Bolt T-Shirt' to cart
        time.sleep(3)
        bolt_tshirt_add_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
        bolt_tshirt_add_btn.click()

        # Verify cart count is '1'
        time.sleep(3)
        cart_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        assert cart_count.text == '1'

        sys.exit(0)

    except Exception as e:
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error_screenshot.png")
        sys.exit(1)

    finally:
        time.sleep(3)
        driver.quit()

if __name__ == "__main__":
    main()
