
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import sys

# Initialize WebDriver options
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-features=NetworkService")

try:
    # Initialize WebDriver
    driver = webdriver.Chrome(options=options)
    
    # Open the website
    driver.get("https://saucedemo.com/")
    time.sleep(5)  # Wait for 5 seconds
    
    # Maximize the window
    driver.maximize_window()
    
    # Login to the website
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))).send_keys("standard_user")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(3)
    
    # Add items to the cart
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(3)
    
    # Proceed to Cart
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]/a'))).click()
    time.sleep(3)
    
    # Proceed to checkout
    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
    time.sleep(3)
    
    # Enter checkout information
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]'))).send_keys("Jonnathan")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("K")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("10007")
    time.sleep(3)
    
    # Continue to the next step
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()
    time.sleep(3)
    
    # Verify Payment Information is visible
    payment_info_label = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]')))
    
    if payment_info_label.is_displayed():
        # Save screenshot
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")
        sys.exit(0)
    else:
        sys.exit(1)

except Exception as e:
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error_screenshot.png")
    sys.exit(1)
finally:
    # Close WebDriver
    driver.quit()
