
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_checkout_payment_information():
    try:
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_argument("--incognito")
        options.add_argument("--disable-features=NetworkService")

        driver = webdriver.Chrome(options=options)
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()

        # Login
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
        driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

        # Add Bike Light to cart
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        ).click()
        time.sleep(3)

        # Add Fleece Jacket to cart
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)

        # Go to Cart
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        time.sleep(3)

        # Proceed to Checkout
        driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
        time.sleep(3)

        # Enter Checkout Information
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]'))
        ).send_keys("Jonnathan")
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("K")
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("10007")
        time.sleep(3)

        # Continue to Payment
        driver.find_element(By.XPATH, '//*[@id="continue"]').click()
        time.sleep(3)

        # Verify Payment Information is visible
        payment_info = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]'))
        )

        assert payment_info.is_displayed()
        
        # Save screenshot
        driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png')

        driver.quit()
        sys.exit(0)
        
    except Exception as e:
        driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error_screenshot.png')
        driver.quit()
        sys.exit(1)

test_checkout_payment_information()
