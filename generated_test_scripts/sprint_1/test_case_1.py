
import time
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
    def login(self, username, password):
        user_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='user-name']"))
        )
        pass_input = self.driver.find_element(By.XPATH, "//input[@id='password']")
        login_button = self.driver.find_element(By.XPATH, "//input[@id='login-button']")
        
        user_input.send_keys(username)
        pass_input.send_keys(password)
        login_button.click()

def main():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-features=NetworkService")
        
        # Initialize the driver
        driver = webdriver.Chrome(options=chrome_options)
        
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        
        driver.maximize_window()
        
        # Login
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        time.sleep(3)

        # Add 'Bike Light' and 'Fleece Jacket' to the cart
        bike_light_add_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))
        )
        fleece_jacket_add_button = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
        
        bike_light_add_button.click()
        time.sleep(3)
        fleece_jacket_add_button.click()
        time.sleep(3)
        
        # Verify cart badge count is '2'
        cart_badge = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
        assert cart_badge.text == "2"
        
        # Remove 'Bike Light'
        remove_bike_light_button = driver.find_element(By.XPATH, "//button[@id='remove-sauce-labs-bike-light']")
        remove_bike_light_button.click()
        time.sleep(3)
        
        # Remove 'Fleece Jacket'
        remove_fleece_jacket_button = driver.find_element(By.XPATH, "//button[@id='remove-sauce-labs-fleece-jacket']")
        remove_fleece_jacket_button.click()
        time.sleep(3)
        
        # Verify cart count element shouldn't exist
        WebDriverWait(driver, 10).until_not(
            EC.presence_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']"))
        )
        
        # Add 'Bolt T-Shirt' to the cart
        bolt_tshirt_add_button = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
        bolt_tshirt_add_button.click()
        time.sleep(3)
        
        # Verify cart badge count is '1'
        cart_badge = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
        assert cart_badge.text == "1"

        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
        
        driver.quit()
        sys.exit(0)
    
    except Exception as e:
        if driver:
            driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
            driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    main()
