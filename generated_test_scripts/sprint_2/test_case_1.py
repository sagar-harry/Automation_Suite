
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_purchase_flow():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--incognito')
    options.add_argument('--disable-features=NetworkService')
    
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()

        # Login to the application
        login(driver)
        
        # Add 'Bike Light' to the cart
        time.sleep(3)
        wait_for_element(driver, By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()

        # Add 'Fleece Jacket' to the cart
        time.sleep(3)
        wait_for_element(driver, By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()

        # Click on the cart icon
        time.sleep(3)
        wait_for_element(driver, By.XPATH, '//*[@id="shopping_cart_container"]/a').click()

        # Proceed to checkout
        time.sleep(3)
        wait_for_element(driver, By.XPATH, '//*[@id="checkout"]').click()

        # Enter checkout information
        time.sleep(3)
        wait_for_element(driver, By.XPATH, '//*[@id="first-name"]').send_keys('somename')
        time.sleep(3)
        wait_for_element(driver, By.XPATH, '//*[@id="last-name"]').send_keys('lastname')
        time.sleep(3)
        wait_for_element(driver, By.XPATH, '//*[@id="postal-code"]').send_keys('123456')

        # Continue and complete the purchase
        time.sleep(3)
        wait_for_element(driver, By.XPATH, '//*[@id="continue"]').click()
        time.sleep(3)
        wait_for_element(driver, By.XPATH, '//*[@id="finish"]').click()

        # Back to products
        time.sleep(3)
        wait_for_element(driver, By.XPATH, '//*[@id="back-to-products"]').click()

        # Logout
        time.sleep(3)
        wait_for_element(driver, By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
        time.sleep(3)
        wait_for_element(driver, By.XPATH, '//*[@id="logout_sidebar_link"]').click()

        # Checking successful logout might require validations if possible
        sys.exit(0)

    except Exception as e:
        print("Test Failed:", e)
        sys.exit(1)

    finally:
        driver.quit()

def login(driver):
    time.sleep(3)
    wait_for_element(driver, By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    time.sleep(3)
    wait_for_element(driver, By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    time.sleep(3)
    wait_for_element(driver, By.XPATH, '//*[@id="login-button"]').click()

def wait_for_element(driver, by, value):
    return WebDriverWait(driver, 10).until(EC.visibility_of_element_located((by, value)))

if __name__ == "__main__":
    test_purchase_flow()
