
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_purchase_flow():
    try:
        # Set up Chrome options
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-features=NetworkService")
        
        # Initialize the WebDriver
        driver = webdriver.Chrome(options=chrome_options)
        
        # Open the website
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()

        # Login
        wait = WebDriverWait(driver, 10)
        driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

        # Add items to cart
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()

        # Checkout process
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="checkout"]'))).click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("somename")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("lastname")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("123456")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="continue"]').click()

        # Finish purchase
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="finish"]'))).click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()

        # Logout
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-burger-menu-btn"]'))).click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()

        # Save screenshot
        script_name = __file__.split('/')[-1].split('.')[0]
        driver.save_screenshot(f"C:/Users/Administrator/Desktop/QE_COE/automated_pipeline_2/captured_screenshots/{script_name}_screenshot.png")

        driver.quit()
        sys.exit(0)
        
    except Exception as e:
        print(f"Test failed: {e}")
        driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    test_purchase_flow()
