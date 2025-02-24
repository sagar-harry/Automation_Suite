
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import sys

def run_test():
    try:
        # Initialize Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-features=NetworkService")

        # Path to chromedriver
        driver_path = "path/to/chromedriver"
        driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

        try:
            # Open the website
            driver.get("https://saucedemo.com/")
            driver.maximize_window()
            time.sleep(5)

            # Log in
            driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
            time.sleep(3)
            driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
            time.sleep(3)
            driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
            time.sleep(3)

            # Add items to the cart
            driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
            time.sleep(3)
            driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
            time.sleep(3)

            # Go to cart and proceed to checkout
            driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
            time.sleep(3)
            driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
            time.sleep(3)

            # Enter checkout information
            driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("somename")
            time.sleep(3)
            driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("lastname")
            time.sleep(3)
            driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("123456")
            time.sleep(3)
            driver.find_element(By.XPATH, '//*[@id="continue"]').click()
            time.sleep(3)

            # Complete purchase
            driver.find_element(By.XPATH, '//*[@id="finish"]').click()
            time.sleep(3)

            # Return to homepage and log out
            driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()
            time.sleep(3)
            driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
            time.sleep(3)
            driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()
            time.sleep(3)

            # Test passed
            sys.exit(0)
        finally:
            driver.quit()
    except Exception as e:
        print(f"Test Failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_test()
