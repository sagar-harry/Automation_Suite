
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

# Setup Selenium with Chrome in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-features=NetworkService")

try:
    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    
    # Open the website
    driver.get("https://saucedemo.com/")
    time.sleep(5)  # Wait for 5 secs after opening the page
    
    # Maximize the page
    driver.maximize_window()
    
    # Define locators
    loc_username = (By.XPATH, '//*[@id="user-name"]')
    loc_password = (By.XPATH, '//*[@id="password"]')
    loc_login = (By.XPATH, '//*[@id="login-button"]')
    loc_bike_light = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
    loc_fleece_jacket = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
    loc_cart_count = (By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    
    # Login with valid credentials
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc_username)).send_keys("standard_user")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc_password)).send_keys("secret_sauce")
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(loc_login)).click()
    time.sleep(3)
    
    # Add 'Bike Light' to the cart
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(loc_bike_light)).click()
    time.sleep(3)
    
    # Add 'Fleece Jacket' to the cart
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(loc_fleece_jacket)).click()
    time.sleep(3)
    
    # Verify the cart badge displays '2'
    cart_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc_cart_count))
    if cart_count.text != '2':
        raise AssertionError("Cart badge count is incorrect after adding two items")
    
    # Reset the cart by removing added products
    driver.get("https://saucedemo.com/cart.html")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]').click()
    driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(3)
    
    # Verify the cart is empty
    cart_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc_cart_count))
    if cart_count.text != '':
        raise AssertionError("Cart is not empty after reset")
    
    # Add 'Bolt T-Shirt' to the cart after reset
    driver.get("https://saucedemo.com/")
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(loc_fleece_jacket)).click()
    time.sleep(3)
    
    # Verify the cart badge displays '1'
    cart_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc_cart_count))
    if cart_count.text != '1':
        raise AssertionError("Cart badge count is incorrect after adding 'Bolt T-Shirt' post reset")
    
    print("Test passed successfully.")
    sys.exit(0)

except Exception as e:
    print(f"Test failed: {str(e)}")
    sys.exit(1)

finally:
    # Close the WebDriver session
    driver.quit()
