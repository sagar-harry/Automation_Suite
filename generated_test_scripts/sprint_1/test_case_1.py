
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome options to disable notifications, run in incognito, and disable network service
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-features=NetworkService")

try:
    # Initialize Chrome driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://saucedemo.com/")
    
    # Wait after opening the page
    time.sleep(5)
    
    # Wait for the login elements and perform login
    wait = WebDriverWait(driver, 10)
    username_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]')))
    password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
    login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    time.sleep(3)
    login_button.click()
    
    # Wait for and add 'Bike Light' to the cart
    bike_light_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
    time.sleep(3)
    bike_light_button.click()
    
    # Wait for and add 'Fleece Jacket' to the cart
    fleece_jacket_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')))
    time.sleep(3)
    fleece_jacket_button.click()
    
    # Verify the cart badge displays '2'
    cart_badge = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
    assert cart_badge.text == '2'
    
    # Remove 'Bike Light' from the cart
    remove_bike_light_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]')))
    time.sleep(3)
    remove_bike_light_button.click()
    
    # Remove 'Fleece Jacket' from the cart
    remove_fleece_jacket_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]')))
    time.sleep(3)
    remove_fleece_jacket_button.click()
    
    # Verify the cart count element doesn't exist
    assert not driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    
    # Add 'Bolt T-Shirt' to the cart
    bolt_tshirt_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
    time.sleep(3)
    bolt_tshirt_button.click()
    
    # Verify the cart badge displays '1'
    cart_badge = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
    assert cart_badge.text == '1'
    
    # Save a snapshot of the page
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")

    # Exit with a status code indicating success
    sys.exit(0)
    
except Exception as e:
    print(f"Test failed: {e}")
    # Save a snapshot in case of failure
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot_failure.png")
    sys.exit(1)
finally:
    # Close the browser
    driver.quit()
