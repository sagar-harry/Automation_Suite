
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

try:
    # Chrome options setup
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-features=NetworkService")

    # Initialize driver
    driver = webdriver.Chrome(options=chrome_options)
    
    # Open the login page
    driver.get("https://saucedemo.com/")
    time.sleep(5)  # Wait for the page to load
    driver.maximize_window()
    
    # Wait for and perform login
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user"]')))
    driver.find_element(By.XPATH, '//*[@id="user"]').send_keys("standard")
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

    # Wait and add 'Bike Light' to the cart
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    
    # Wait and add 'Fleece Jacket' to the cart
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    
    # Click on the cart icon
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="123"]/a').click()
    
    # Proceed to checkout
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout"]')))
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
    
    # Enter checkout information
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]')))
    driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("Jonnathan")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("K")
    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("10007")
    
    # Continue with the order
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()
    
    # Finish the purchase
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="finish"]')))
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="finish"]').click()
    
    # Click on back to products
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="back-to-products"]')))
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()
    
    # Logout from the account
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-burger-menu-btn"]')))
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()

    # Save screenshot
    driver.save_screenshot("C:/Users/Administrator/Desktop/QE_COE/automated_pipeline_2/captured_screenshots/screenshot.png")
    
    # Close the browser
    driver.quit()
    
    sys.exit(0)

except Exception as e:
    print(f"Test case failed due to: {e}")
    driver.save_screenshot("C:/Users/Administrator/Desktop/QE_COE/automated_pipeline_2/captured_screenshots/failure_screenshot.png")
    driver.quit()
    sys.exit(1)
