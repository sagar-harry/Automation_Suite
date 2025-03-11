
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_cart_functionality():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popups")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)
    driver.get("https://saucedemo.com/")
    driver.maximize_window()
    time.sleep(5)

    try:
        # Log in to the application
        def login(username, password):
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))).send_keys(username)
            time.sleep(3)
            driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
            time.sleep(3)
            driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
            time.sleep(3)

        login("standard_user", "secret_sauce")

        # Add 'Bike Light' and 'Fleece Jacket' to the cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]'))).click()
        time.sleep(3)

        # Validate cart count is '2'
        cart_count_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        assert cart_count_element.text == '2'
        
        # Remove 'Bike Light' and 'Fleece Jacket'
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]'))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]'))).click()
        time.sleep(3)
        
        # Validate cart count element doesn't exist
        WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))

        # Add 'Bolt T-Shirt' to the cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
        time.sleep(3)

        # Validate cart count is '1'
        cart_count_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        assert cart_count_element.text == '1'
        
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\cart_functionality_test.png")
        sys.exit(0)
        
    except Exception as e:
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error.png")
        sys.exit(1)
        
    finally:
        driver.quit()

test_cart_functionality()
