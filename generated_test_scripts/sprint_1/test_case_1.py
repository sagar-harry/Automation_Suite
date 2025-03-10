
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

try:
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    # Navigate to the website
    driver.get("https://saucedemo.com/")
    time.sleep(5)  # Initial wait after opening the page

    # Logging in using the LoginPage class
    username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]')))
    password = driver.find_element(By.XPATH, '//*[@id="password"]')
    login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')

    username.send_keys("standard_user")
    time.sleep(3)  # Wait before next action
    password.send_keys("secret_sauce")
    time.sleep(3)  # Wait before next action
    login_button.click()

    time.sleep(3)  # Wait after logging in

    # Add 'Bike Light' and 'Fleece Jacket' to the cart
    bike_light = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
    fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')
    
    bike_light.click()
    time.sleep(3)  # Wait before next action
    fleece_jacket.click()
    time.sleep(3)  # Wait before next action

    # Verify cart badge displays '2'
    cart_badge = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
    assert cart_badge.text == '2', "Cart badge count is not 2"

    # Remove 'Bike Light' and 'Fleece Jacket'
    remove_bike_light = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]')))
    remove_fleece_jacket = driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]')
    
    remove_bike_light.click()
    time.sleep(3)  # Wait before next action
    remove_fleece_jacket.click()
    time.sleep(3)  # Wait before next action

    # Verify the cart count element shouldn't exist
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))

    # Add 'Bolt T-Shirt' to the cart
    add_bolt_tshirt = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
    add_bolt_tshirt.click()
    time.sleep(3)  # Wait before next action

    # Verify cart badge displays '1'
    cart_badge = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
    assert cart_badge.text == '1', "Cart badge count is not 1"

    # Save snapshot of the page
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")

    sys.exit(0)

except Exception as e:
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error_screenshot.png")
    print(f"Test failed: {e}")
    sys.exit(1)

finally:
    driver.quit()
