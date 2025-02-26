
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def main():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_argument("--disable-features=NetworkService")
    
    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    
    try:
        # Open the website
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()

        # Login
        driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

        # Add items to the cart
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        
        # Go to cart
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()

        # Checkout process
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
        
        # Enter user information
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]'))).send_keys("somename")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("lastname")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("123456")
        
        # Continue checkout
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="continue"]').click()
        
        # Finish purchase
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="finish"]'))).click()

        # Back to homepage
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()
        
        # Log out of the application
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()
        
        sys.exit(0)
    
    except Exception as e:
        print(f"Test Failed: {e}")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
