
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time
import os

# Initialize Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-features=NetworkService")

try:
    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    
    # Open the website
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    
    # Login
    from LoginPage import login
    login(driver, "standard_user", "secret_sauce")
    time.sleep(3)
    
    # Add Bike Light to cart
    bike_light = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
    )
    bike_light.click()
    time.sleep(3)
    
    # Add Fleece Jacket to cart
    fleece_jacket = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]'))
    )
    fleece_jacket.click()
    time.sleep(3)
    
    # Check cart badge count
    cart_badge = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
    )
    assert cart_badge.text == '2', "Cart badge count does not match expected value"
    time.sleep(3)
    
    # Remove Bike Light
    remove_bike_light = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]'))
    )
    remove_bike_light.click()
    time.sleep(3)
    
    # Remove Fleece Jacket
    remove_fleece_jacket = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]'))
    )
    remove_fleece_jacket.click()
    time.sleep(3)
    
    # Verify cart count element does not exist
    assert not WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
    ), "Cart count badge should not exist after removing all items"
    time.sleep(3)
    
    # Add Bolt T-Shirt to cart
    bolt_tshirt = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
    )
    bolt_tshirt.click()
    time.sleep(3)
    
    # Check cart badge count again
    cart_badge = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
    )
    assert cart_badge.text == '1', "Cart badge count does not match expected value after adding Bolt T-Shirt"
    time.sleep(3)
    
    # Save page snapshot
    os.makedirs("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots", exist_ok=True)
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\page_snapshot.png")
    
    sys.exit(0)
    
except Exception as e:
    # Save page snapshot in case of failure
    os.makedirs("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots", exist_ok=True)
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\failure_snapshot.png")
    print(str(e))
    sys.exit(1)
finally:
    # Quit the driver
    driver.quit()
