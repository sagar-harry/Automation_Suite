
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

try:
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-features=NetworkService")
    
    # Initialize driver
    driver = webdriver.Chrome(options=chrome_options)
    
    # Open the website
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    
    # Maximize the window
    driver.maximize_window()
    
    # Wait function for elements
    def wait_for_element(xpath):
        return WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
    
    # Login
    wait_for_element('//*[@id="user-name"]').send_keys("standard_user")
    time.sleep(3)
    wait_for_element('//*[@id="password"]').send_keys("secret_sauce")
    time.sleep(3)
    wait_for_element('//*[@id="login-button"]').click()
    time.sleep(3)
    
    # Add items to the cart
    wait_for_element('//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    time.sleep(3)
    wait_for_element('//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(3)
    
    # Navigate to cart and proceed to checkout
    wait_for_element('//*[@id="shopping_cart_container"]/a').click()
    time.sleep(3)
    wait_for_element('//*[@id="checkout"]').click()
    time.sleep(3)
    
    # Enter customer information
    wait_for_element('//*[@id="first-name"]').send_keys("Jonnathan")
    time.sleep(3)
    wait_for_element('//*[@id="last-name"]').send_keys("K")
    time.sleep(3)
    wait_for_element('//*[@id="postal-code"]').send_keys("10007")
    time.sleep(3)
    wait_for_element('//*[@id="continue"]').click()
    time.sleep(3)
    
    # Complete the purchase
    wait_for_element('//*[@id="finish"]').click()
    time.sleep(3)
    
    # Return to the homepage
    wait_for_element('//*[@id="back-to-products"]').click()
    time.sleep(3)
    
    # Log out
    wait_for_element('//*[@id="react-burger-menu-btn"]').click()
    time.sleep(3)
    wait_for_element('//*[@id="logout_sidebar_link"]').click()
    time.sleep(3)
    
    # Test successful
    sys.exit(0)

except Exception as e:
    # Save a screenshot if test fails
    driver.save_screenshot("C:/Users/Administrator/Desktop/QE_COE/automated_pipeline_2/captured_screenshots/test_failure.png")
    sys.exit(1)

finally:
    driver.quit()
