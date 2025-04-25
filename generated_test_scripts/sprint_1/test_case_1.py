
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

# Configure Chrome options
options = Options()
options.add_argument("--incognito")
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-features=NetworkService")

try:
    # Start the webdriver
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    
    # Open the URL and wait
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    
    # Login
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(3)
    
    # Add 'Bike Light' to the cart
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
    ).click()
    time.sleep(3)
    
    # Add 'Fleece Jacket' to the cart
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]'))
    ).click()
    time.sleep(3)
    
    # Verify cart badge shows '2'
    cart_badge = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
    )
    assert cart_badge.text == '2', "Cart badge does not display '2'"

    # Remove 'Bike Light'
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]'))
    ).click()
    time.sleep(3)
    
    # Remove 'Fleece Jacket'
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]'))
    ).click()
    time.sleep(3)
    
    # Verify cart count element does not exist
    assert not driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span'), "Cart count element exists"
    
    # Add 'Bolt T-Shirt' to the cart
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
    ).click()
    time.sleep(3)
    
    # Verify cart badge shows '1'
    cart_badge = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
    )
    assert cart_badge.text == '1', "Cart badge does not display '1'"
    
    # Save screenshot
    driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png')
    
    sys.exit(0)

except Exception as e:
    print(f"Test case failed: {e}")
    driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png')
    sys.exit(1)

finally:
    driver.quit()
