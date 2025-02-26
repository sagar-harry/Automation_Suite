
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

# Initialize options for Chrome browser
options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--incognito")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-features=NetworkService")

try:
    # Launch the browser
    driver = webdriver.Chrome(options=options)
    driver.get("https://saucedemo.com/")
    sleep(5)
    driver.maximize_window()
    
    # Login
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))).send_keys("standard_user")
    sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys("secret_sauce")
    sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]'))).click()

    # Add 'Bike Light' to the cart
    sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
    
    # Add 'Fleece Jacket' to the cart
    sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]'))).click()

    # Verify cart badge counter
    sleep(3)
    cart_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
    assert cart_count.text == '2', "Cart count should be 2"
    
    # Remove 'Bike Light'
    sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]'))).click()
    
    # Remove 'Fleece Jacket'
    sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]'))).click()

    # Verify cart count element doesn't exist
    sleep(3)
    cart_count_elements = driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    assert len(cart_count_elements) == 0, "Cart count element should not exist"

    # Add 'Bolt T-Shirt' to cart
    sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()

    # Verify cart badge counter
    sleep(3)
    cart_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
    assert cart_count.text == '1', "Cart count should be 1"

    # Save the screenshot
    driver.save_screenshot("C:/Users/Administrator/Desktop/QE_COE/automated_pipeline_2/captured_screenshots/test_ui_script.png")
    
    sys.exit(0)
except Exception as e:
    print(f"Test failed: {str(e)}")
    sys.exit(1)
finally:
    driver.quit()
