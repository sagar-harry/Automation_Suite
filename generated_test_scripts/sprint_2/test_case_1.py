
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def run_test():
    try:
        options = Options()
        options.add_argument("--incognito")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-features=NetworkService")
        
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        wait = WebDriverWait(driver, 10)
        
        # Login
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))).send_keys("standard_user")
        time.sleep(3)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys("secret_sauce")
        time.sleep(3)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login-button"]'))).click()
        time.sleep(3)

        # Add items to cart
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
        time.sleep(3)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
        time.sleep(3)
        
        # Proceed to cart and checkout
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a'))).click()
        time.sleep(3)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout"]'))).click()
        time.sleep(3)

        # Fill out checkout information
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]'))).send_keys("somename")
        time.sleep(3)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="last-name"]'))).send_keys("lastname")
        time.sleep(3)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="postal-code"]'))).send_keys("123456")
        time.sleep(3)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="continue"]'))).click()
        time.sleep(3)

        # Complete the purchase
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="finish"]'))).click()
        time.sleep(3)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="back-to-products"]'))).click()
        time.sleep(3)

        # Logout
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-burger-menu-btn"]'))).click()
        time.sleep(3)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="logout_sidebar_link"]'))).click()
        time.sleep(3)

        # Capture final screenshot
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")
        
        # Ensure clean exit
        driver.quit()
        sys.exit(0)

    except Exception as e:
        if driver:
            driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error_screenshot.png")
            driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    run_test()
