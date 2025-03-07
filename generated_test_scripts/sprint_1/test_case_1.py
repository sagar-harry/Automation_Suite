
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_argument("--incognito")
options.add_argument("--disable-features=NetworkService")

driver = webdriver.Chrome(options=options)

try:
    driver.maximize_window()
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    
    # Login
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
    )
    time.sleep(3)
    
    # Add Bike Light
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    time.sleep(3)
    
    # Add Fleece Jacket
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
    )
    time.sleep(3)
    
    # Verify Cart Count = 2
    cart_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    if not cart_badge.text == '2':
        raise Exception("Cart Count is not 2 after adding items")
    
    # Remove Bike Light
    driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]').click()
    time.sleep(3)
    
    # Remove Fleece Jacket
    driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]').click()
    
    time.sleep(3)
    # Verify Cart Badge does not exist
    cart_badge_elements = driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    if len(cart_badge_elements) > 0:
        raise Exception("Cart Badge still exists after removing items")
    
    # Add Bolt T-Shirt
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
    )
    time.sleep(3)
    
    # Verify Cart Count = 1
    cart_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    if not cart_badge.text == '1':
        raise Exception("Cart Count is not 1 after adding Bolt T-Shirt")
    
    # Success
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\success.png")
    sys.exit(0)

except Exception as e:
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\failure.png")
    sys.exit(1)

finally:
    driver.quit()
