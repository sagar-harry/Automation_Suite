
import sys
import time
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run_test():
    try:
        # Setup Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-features=NetworkService")

        # Initialize the driver
        driver = webdriver.Chrome(options=chrome_options)

        try:
            # Maximize the window
            driver.maximize_window()

            # Navigate to the website
            driver.get("https://saucedemo.com/")
            time.sleep(5)

            # Login
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="user"]'))
            ).send_keys("standard")
            time.sleep(3)

            driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
            time.sleep(3)

            driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
            time.sleep(3)

            # Add 'Bike Light' to cart
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
            ).click()
            time.sleep(3)

            # Add 'Fleece Jacket' to cart
            driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
            time.sleep(3)

            # Click on the cart icon
            driver.find_element(By.XPATH, '//*[@id="123"]/a').click()
            time.sleep(3)

            # Proceed to checkout
            driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
            time.sleep(3)

            # Enter First Name, Last Name and Zip Code
            driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("Jonnathan")
            time.sleep(3)

            driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("K")
            time.sleep(3)

            driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("10007")
            time.sleep(3)

            # Continue and complete purchase
            driver.find_element(By.XPATH, '//*[@id="continue"]').click()
            time.sleep(3)

            driver.find_element(By.XPATH, '//*[@id="finish"]').click()
            time.sleep(3)

            # Return to homepage
            driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()
            time.sleep(3)

            # Logout
            driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
            time.sleep(3)

            driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()
            time.sleep(3)

            # Save a snapshot
            driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\homepage.png")

            sys.exit(0)
        finally:
            # Tear down the driver
            driver.quit()
    except Exception as e:
        print("An error occurred:", e)
        print(traceback.format_exc())
        sys.exit(1)

if __name__ == "__main__":
    run_test()
