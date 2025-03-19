
import sys
import time
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=NetworkService")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver

def login(driver):
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(3)

def perform_test():
    driver = setup_driver()
    try:
        login(driver)
        
        # Add bike light to cart
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)
        
        # Add fleece jacket to cart
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()
        time.sleep(3)
        
        # Verify cart badge for 2 items
        cart_badge = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        assert cart_badge.text == "2"
        
        # Remove bike light from cart
        driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]').click()
        time.sleep(3)
        
        # Remove fleece jacket from cart
        driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]').click()
        time.sleep(3)
        
        # Verify cart count element shouldn't exist
        assert not driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        
        # Add Bolt T-Shirt to cart
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)
        
        # Verify cart badge for 1 item
        cart_badge = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        assert cart_badge.text == "1"
        
        # Save snapshot of the page
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\test_result.png")
        
        sys.exit(0)
    except Exception as e:
        traceback.print_exc()
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error.png")
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    perform_test()
