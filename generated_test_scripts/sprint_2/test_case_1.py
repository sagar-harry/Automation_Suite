
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Test Case: Validate complete purchase flow on SauceDemo
def test_purchase_flow():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-features=NetworkService")
        
        driver = webdriver.Chrome(options=options)
        driver.get("https://saucedemo.com/")
        time.sleep(5)  # Wait for 5 secs after opening the page
        driver.maximize_window()
        
        # Login
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='user-name']"))).send_keys("standard_user")
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password']"))).send_keys("secret_sauce")
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']"))).click()
        time.sleep(3)
        
        # Add items to cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"))).click()
        time.sleep(3)
        
        # Proceed to checkout
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='shopping_cart_link']"))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='checkout']"))).click()
        time.sleep(3)
        
        # Enter shipping details
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='first-name']"))).send_keys("Jonnathan")
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='last-name']"))).send_keys("K")
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='postal-code']"))).send_keys("10007")
        time.sleep(3)
        
        # Continue and complete purchase
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='continue']"))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='finish']"))).click()
        time.sleep(3)
        
        # Return to homepage and logout
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='back-to-products']"))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='react-burger-menu-btn']"))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='logout_sidebar_link']"))).click()
        time.sleep(3)
        
        sys.exit(0)  # Exit with success code 0

    except Exception as e:
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
        sys.exit(1)  # Exit with failure code 1

    finally:
        driver.quit()

test_purchase_flow()
