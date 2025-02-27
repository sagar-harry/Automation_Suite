
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-features=NetworkService")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://saucedemo.com/")
driver.maximize_window()
time.sleep(5)  # Wait for 5 seconds

try:
    # Login
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    
    time.sleep(3)  # Wait for 3 seconds
    
    # Add items to cart
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
    ).click()
    time.sleep(3)  # Wait for 3 seconds
    
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
    ).click()
    time.sleep(3)  # Wait for 3 seconds
    
    # Go to cart
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a'))
    ).click()
    time.sleep(3)  # Wait for 3 seconds
    
    # Proceed to checkout
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout"]'))
    ).click()
    time.sleep(3)  # Wait for 3 seconds

    # Enter checkout details
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]'))
    ).send_keys('somename')
    
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="last-name"]'))
    ).send_keys('lastname')
    
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="postal-code"]'))
    ).send_keys('123456')
    
    time.sleep(3)  # Wait for 3 seconds
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="continue"]'))
    ).click()
    
    time.sleep(3)  # Wait for 3 seconds

    # Verify payment information is visible
    payment_info_visible = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]'))
    )
    
    if payment_info_visible:
        print("Test case passed. Payment Information section is visible.")
        driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\checkout_summary.png')
        sys.exit(0)  # Test case passed

except Exception as e:
    print(f"Test case failed due to: {str(e)}")
    driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error.png')
    sys.exit(1)  # Test case failed

finally:
    driver.quit()
