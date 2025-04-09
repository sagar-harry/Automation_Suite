
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-features=NetworkService")

try:
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    
    # Login
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]')))
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    
    # Add items to cart
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()

    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')))
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()

    # Check cart count
    time.sleep(3)
    cart_count = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
    assert cart_count.text == '2'

    # Remove items and verify cart badge disappears
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]').click()
    
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]').click()
    
    time.sleep(3)
    WebDriverWait(driver, 10).until_not(
        EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))

    # Add Bolt T-Shirt to cart
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()

    # Check cart count
    time.sleep(3)
    cart_count = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
    assert cart_count.text == '1'

    # Test Pass
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\snapshot.png")
    sys.exit(0)

except Exception as e:
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\snapshot.png")
    sys.exit(1)

finally:
    time.sleep(3)
    driver.quit()
