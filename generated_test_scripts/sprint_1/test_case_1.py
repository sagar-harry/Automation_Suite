
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import sys

def test_shopping_cart():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-notifications')
        options.add_argument('--disable-popup-blocking')
        options.add_argument('--incognito')
        options.add_argument('--disable-features=NetworkService')

        driver = webdriver.Chrome(options=options)
        driver.get('https://saucedemo.com/')
        
        time.sleep(5)  # wait for the page to load
        driver.maximize_window()

        # Login
        driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
        driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        time.sleep(3)
        
        # Add Bike Light to cart
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()

        time.sleep(3)
        
        # Add Fleece Jacket to cart
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()

        time.sleep(3)
        
        # Verify cart displays '2'
        cart_badge = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        assert cart_badge.text == '2', "Cart badge does not display 2"

        time.sleep(3)

        # Remove Bike Light
        driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]').click()

        time.sleep(3)

        # Remove Fleece Jacket
        driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]').click()

        time.sleep(3)

        # Verify cart badge does not exist
        try:
            cart_badge_present = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
            assert False, "Cart badge is still present"
        except Exception:
            pass

        # Add Bolt T-Shirt to cart
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()

        time.sleep(3)

        # Verify cart displays '1'
        cart_badge = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        assert cart_badge.text == '1', "Cart badge does not display 1"

        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
        driver.quit()
        sys.exit(0)
        
    except Exception as e:
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
        driver.quit()
        sys.exit(1)

test_shopping_cart()
