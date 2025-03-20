
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import sys

def test_purchase_flow():
    try:
        options = Options()
        options.add_argument('--incognito')
        options.add_argument('--disable-notifications')
        options.add_argument('--disable-popup-blocking')
        options.add_argument('--disable-features=NetworkService')

        driver = webdriver.Chrome(options=options)
        driver.get('https://saucedemo.com/')
        time.sleep(5)
        driver.maximize_window()
        
        # Login
        driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(3)
        
        # Add items to cart
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)
        
        # View cart and checkout
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
        time.sleep(3)

        # Fill out user information
        driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('Jonnathan')
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('K')
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys('10007')
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="continue"]').click()
        time.sleep(3)

        # Complete purchase
        driver.find_element(By.XPATH, '//*[@id="finish"]').click()
        time.sleep(3)

        # Go back to the homepage
        driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()
        time.sleep(3)

        # Logout
        driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()
        time.sleep(3)

        # Take screenshot before closing
        driver.save_screenshot('C:/Users/Administrator/Desktop/QE_COE/automated_pipeline_2/captured_screenshots/screenshot.png')
        
        driver.quit()
        sys.exit(0)

    except Exception as e:
        driver.save_screenshot('C:/Users/Administrator/Desktop/QE_COE/automated_pipeline_2/captured_screenshots/screenshot_error.png')
        driver.quit()
        sys.exit(1)

test_purchase_flow()
