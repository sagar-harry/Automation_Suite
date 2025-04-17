
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options
options = Options()
options.add_argument("--incognito")
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-features=NetworkService")

try:
    # Initialize the Chrome driver
    driver = webdriver.Chrome(options=options)
    
    # Maximize the window and navigate to the website
    driver.maximize_window()
    driver.get("https://saucedemo.com/")
    time.sleep(5) # Wait 5 seconds as specified
    
    # Login
    username = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]')))
    password = driver.find_element(By.XPATH, '//*[@id="password"]')
    login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    
    username.send_keys('standard_user')
    time.sleep(3) # Wait 3 seconds before every action
    password.send_keys('secret_sauce')
    time.sleep(3)
    login_button.click()

    # Add 'Bike Light' and 'Fleece Jacket' to the cart
    bike_light = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
    fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')
    
    bike_light.click()
    time.sleep(3)
    fleece_jacket.click()
    time.sleep(3)

    # Verify cart badge displays '2'
    cart_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
    assert cart_count.text == '2', "Cart count is not 2"

    # Remove 'Bike Light' and 'Fleece Jacket'
    remove_bike_light = driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]')
    remove_fleece_jacket = driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]')
    
    remove_bike_light.click()
    time.sleep(3)
    remove_fleece_jacket.click()
    time.sleep(3)

    # Verify cart count element does not exist
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))

    # Add 'Bolt T-Shirt' to the cart
    add_bolt_t_shirt = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
    add_bolt_t_shirt.click()
    time.sleep(3)

    # Verify cart badge displays '1'
    cart_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
    assert cart_count.text == '1', "Cart count is not 1"

    # Take a screenshot of the page
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\final_screenshot.png")

    # If we reach this point, the tests have passed
    sys.exit(0)
    
except Exception as e:
    # If any error occurs, exit with code 1
    print(f"Test failed: {e}")
    sys.exit(1)

finally:
    # Always close the driver
    driver.quit()
