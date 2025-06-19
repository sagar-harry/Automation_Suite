
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import sys

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-features=NetworkService")

try:
    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    
    # Open the website URL
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    
    # Maximize the window
    driver.maximize_window()

    # Login to the application
    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()
    
    # Add 'Bike Light' to the cart
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))
    ).click()
    time.sleep(3)
    
    # Add 'Fleece Jacket' to the cart
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"))
    ).click()
    time.sleep(3)
    
    # Verify cart badge displays '2'
    cart_badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']"))
    )
    assert cart_badge.text == '2'
    time.sleep(3)
    
    # Remove 'Bike Light'
    driver.find_element(By.XPATH, "//button[@id='remove-sauce-labs-bike-light']").click()
    time.sleep(3)
    
    # Remove 'Fleece Jacket'
    driver.find_element(By.XPATH, "//button[@id='remove-sauce-labs-fleece-jacket']").click()
    time.sleep(3)
    
    # Verify cart badge doesn't exist
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element((By.XPATH, "//span[@class='shopping_cart_badge']"))
    )
    
    # Add 'Bolt T-Shirt' to the cart
    driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
    time.sleep(3)
    
    # Verify cart badge displays '1'
    cart_badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']"))
    )
    assert cart_badge.text == '1'
    
    # Take screenshot of final state
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\final_state.png")
    
    driver.quit()
    sys.exit(0)

except Exception as e:
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error_state.png")
    driver.quit()
    sys.exit(1)
