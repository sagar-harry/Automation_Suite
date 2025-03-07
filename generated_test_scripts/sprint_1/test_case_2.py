
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import sys
import os
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        time.sleep(3)  # Wait for 3 secs before actions
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

def main():
    try:
        # Setup the chrome options
        options = Options()
        options.add_argument("--incognito")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-features=NetworkService")
        
        # Initialize the WebDriver
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        
        # Open the page
        driver.get("https://saucedemo.com/")
        time.sleep(5)  # Wait for 5 secs after the page opens
        
        # Log in to the application
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        # Add items to cart
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)
        
        # Proceed to checkout
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="checkout"]').click()

        # Enter checkout information
        driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("Jonnathan")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("K")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("10007")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="continue"]').click()
        
        # Verify payment information section is displayed
        time.sleep(3)
        payment_info = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]')
        
        if payment_info.is_displayed():
            print("Test case passed")
            screenshot_path = r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png"
            driver.save_screenshot(screenshot_path)
            sys.exit(0)
        else:
            print("Test case failed")
            sys.exit(1)
    
    except Exception as e:
        print(f"Test failed: {e}")
        if driver:
            screenshot_path = r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png"
            driver.save_screenshot(screenshot_path)
        sys.exit(1)
    
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
