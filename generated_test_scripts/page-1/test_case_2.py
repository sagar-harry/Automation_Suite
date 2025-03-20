
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def login(driver, username, password):
    driver.get('https://saucedemo.com/')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))).send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_argument('--disable-features=NetworkService')
    
    driver = webdriver.Chrome(options=options)

    try:
        driver.maximize_window()
        time.sleep(5)
        
        login(driver, 'standard_user', 'secret_sauce')
        
        time.sleep(3)
        
        # Add Bike Light to Cart
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
        time.sleep(3)
        
        # Add Fleece Jacket to Cart
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]'))).click()
        time.sleep(3)
        
        # Verify Cart Count
        cart_count = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))).text
        assert cart_count == '2', "Cart count is not 2"
        
        # Remove Bike Light
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]'))).click()
        time.sleep(3)
        
        # Remove Fleece Jacket
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]'))).click()
        time.sleep(3)
        
        # Verify Cart Count Element does not exist
        cart_count_elements = driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert not cart_count_elements, "Cart count element should not exist"
        
        # Add Bolt T-Shirt
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
        time.sleep(3)
        
        # Verify Cart Count is 1
        cart_count = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))).text
        assert cart_count == '1', "Cart count is not 1"

        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\final_state.png")

    except Exception as e:
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error_state.png")
        driver.quit()
        sys.exit(1)

    driver.quit()
    sys.exit(0)

if __name__ == "__main__":
    main()
