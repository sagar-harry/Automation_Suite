
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time
import os

try:
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popups")
    options.add_argument("--disable-features=NetworkService")

    # Initialize the Chrome driver
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    # Open the website
    driver.get("https://saucedemo.com/")
    time.sleep(5) # Wait after opening the page

    # Login method
    def login():
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))).send_keys("standard_user")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys("secret_sauce")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]'))).click()

    login()

    time.sleep(3) # Wait before adding items to cart
    # Add Bike Light to the cart
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()

    time.sleep(3) # Wait before adding another item
    # Add Fleece Jacket to the cart
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]'))).click()

    time.sleep(3) # Wait to check cart count
    # Verify cart displays '2'
    badge = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))).text
    assert badge == '2', f"Expected cart count to be 2, but got {badge}"

    time.sleep(3) # Wait before removing items
    # Remove Bike Light
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]'))).click()

    time.sleep(3) # Wait before removing another item
    # Remove Fleece Jacket
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]'))).click()

    time.sleep(3) # Wait to check absence of cart count
    # Verify cart count element shouldn't exist
    assert not driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span'), "Cart count element still exists."

    time.sleep(3) # Wait before adding new item
    # Add Bolt T-Shirt to the cart
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()

    time.sleep(3) # Wait to check cart count again
    # Verify cart displays '1'
    badge = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))).text
    assert badge == '1', f"Expected cart count to be 1, but got {badge}"

    # Save snapshot of the page
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")

    driver.quit()
    sys.exit(0)

except Exception as e:
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error_screenshot.png")
    driver.quit()
    sys.exit(1)
