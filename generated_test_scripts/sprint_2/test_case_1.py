
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def run_test():
    try:
        options = Options()
        options.headless = True
        options.add_argument("--disable-notifications")
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        
        # Open the website
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()
        
        # Log in to the website
        driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(3)
        
        # Add 'Bike Light' to the cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
        time.sleep(3)
        
        # Add 'Fleece Jacket' to the cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
        time.sleep(3)
        
        # Click on the cart icon
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]/a'))).click()
        time.sleep(3)
        
        # Proceed to checkout
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout"]'))).click()
        time.sleep(3)
        
        # Enter First Name, Last Name, and Zip Code
        driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("somename")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("lastname")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("123456")
        time.sleep(3)
        
        # Continue and complete the purchase
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="continue"]'))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="finish"]'))).click()
        time.sleep(3)

        # Return to the homepage
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="back-to-products"]'))).click()
        time.sleep(3)
        
        # Log out
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-burger-menu-btn"]'))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="logout_sidebar_link"]'))).click()
        time.sleep(3)

        # Test case passed
        driver.quit()
        sys.exit(0)
    except Exception as e:
        print(f"Test failed: {e}")
        if 'driver' in locals():
            driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    run_test()
