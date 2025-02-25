
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

try:
    # Set Chrome options
    options = Options()
    options.headless = True
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")

    # Initialize webdriver
    driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(10)

    # Open website
    driver.get("https://saucedemo.com/")
    
    # Maximize window
    driver.maximize_window()
    
    # Wait for page to load
    time.sleep(5)

    # Wait before action
    time.sleep(3)

    # Login
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    
    # Wait before action
    time.sleep(3)

    # Add Bike Light to cart
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
    ).click()

    # Wait before action
    time.sleep(3)

    # Add Fleece Jacket to cart
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
    ).click()
    
    # Wait before action
    time.sleep(3)

    # Click on cart icon
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]/a'))
    ).click()
    
    # Wait before action
    time.sleep(3)

    # Proceed to checkout
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout"]'))
    ).click()
    
    # Wait before action
    time.sleep(3)

    # Enter checkout information
    driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('somename')
    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('lastname')
    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys('123456')
    
    # Wait before action
    time.sleep(3)

    # Continue with checkout
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()
    
    # Wait before action
    time.sleep(3)

    # Finish purchase
    driver.find_element(By.XPATH, '//*[@id="finish"]').click()
    
    # Wait before action
    time.sleep(3)

    # Return to homepage
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="back-to-products"]'))
    ).click()
    
    # Wait before action
    time.sleep(3)

    # Logout process
    driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
    
    # Wait before action
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()
    
    # Test case success
    sys.exit(0)

except Exception as e:
    print(f"Test failed: {e}")
    sys.exit(1)

finally:
    # Close the driver
    driver.quit()
