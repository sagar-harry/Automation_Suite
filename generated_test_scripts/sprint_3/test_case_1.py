
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, sys

def initialize_driver():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=NetworkService")
    
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver

def take_screenshot(driver):
    driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png')

def test_scenario():
    try:
        driver = initialize_driver()
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        
        wait = WebDriverWait(driver, 10)
        
        # Login
        username_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user"]')))
        password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
        
        username_field.send_keys("standard")
        time.sleep(3)
        password_field.send_keys("secret_sauce")
        time.sleep(3)
        login_button.click()

        # Add items to cart
        bike_light = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        
        bike_light.click()
        time.sleep(3)
        fleece_jacket.click()
        time.sleep(3)
        
        # Proceed to checkout
        cart_icon = driver.find_element(By.XPATH, '//*[@id="123"]/a')
        cart_icon.click()
        time.sleep(3)
        checkout_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout"]')))
        checkout_button.click()
        time.sleep(3)
        
        # Enter checkout information
        first_name = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]')))
        last_name = driver.find_element(By.XPATH, '//*[@id="last-name"]')
        postal_code = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
        
        first_name.send_keys("Jonnathan")
        time.sleep(3)
        last_name.send_keys("K")
        time.sleep(3)
        postal_code.send_keys("10007")
        time.sleep(3)
        
        continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
        continue_button.click()
        time.sleep(3)
        
        finish_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="finish"]')))
        finish_button.click()
        time.sleep(3)
        
        back_to_products_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="back-to-products"]')))
        back_to_products_button.click()
        time.sleep(3)
        
        # Logout
        logout_sidebar = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-burger-menu-btn"]')))
        logout_sidebar.click()
        time.sleep(3)
        logout_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="logout_sidebar_link"]')))
        logout_button.click()
        time.sleep(3)
        
        take_screenshot(driver)
        driver.quit()
        sys.exit(0)
    
    except Exception as e:
        take_screenshot(driver)
        driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    test_scenario()
