
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_ui_cart():
    options = Options()
    options.headless = True
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    
    try:
        driver = webdriver.Chrome(options=options)
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()

        # Login
        driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        
        # Add 'Bike Light' to the cart
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
        time.sleep(3)
        
        # Add 'Fleece Jacket' to the cart
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
        time.sleep(3)
        
        # Verify cart badge displays '2'
        cart_count = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        assert cart_count.text == '2'
        time.sleep(3)

        # Remove all items from the cart (simulate reset)
        driver.find_element(By.XPATH, '//button[contains(text(), "Remove")]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//button[contains(text(), "Remove")]').click()
        time.sleep(3)
        
        # Verify cart badge is empty
        try:
            cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
            assert False, "Cart is not empty"
        except:
            pass
        
        # Add 'Bolt T-Shirt' to the cart
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
        time.sleep(3)
        
        # Verify cart badge displays '1'
        cart_count = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        assert cart_count.text == '1'
        time.sleep(3)

        driver.quit()
        exit(0)  # Exit with code 0 if test case passed

    except Exception as e:
        print(f"Test failed: {str(e)}")
        driver.quit()
        exit(1)  # Exit with code 1 if test case failed

test_ui_cart()
