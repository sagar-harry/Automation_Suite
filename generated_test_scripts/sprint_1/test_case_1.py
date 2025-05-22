
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setting Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-features=NetworkService")

# Initiate webdriver
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

try:
    # Open website
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    
    # Wait until username field is available, then log in using the LoginPage class method
    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))
    )
    username.send_keys('standard_user')
    
    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
    )
    password.send_keys('secret_sauce')
    
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]'))
    )
    login_button.click()
    time.sleep(3)

    # Add 'Bike Light' and 'Fleece Jacket' to the cart
    bike_light = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
    )
    bike_light.click()
    time.sleep(3)
    
    fleece_jacket = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]'))
    )
    fleece_jacket.click()
    time.sleep(3)

    # Verify cart badge displays '2'
    cart_count = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
    )
    assert cart_count.text == '2'
    
    # Remove 'Bike Light' and 'Fleece Jacket'
    remove_bike_light = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]'))
    )
    remove_bike_light.click()
    time.sleep(3)

    remove_fleece_jacket = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]'))
    )
    remove_fleece_jacket.click()
    time.sleep(3)

    # Verify cart count element doesn't exist
    try:
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        sys.exit(1)  # Element should not exist, so this is an error
    except NoSuchElementException:
        pass

    # Add 'Bolt T-Shirt' to the cart
    add_bolt_tshirt = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
    )
    add_bolt_tshirt.click()
    time.sleep(3)

    # Verify cart badge displays '1'
    cart_count = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
    )
    assert cart_count.text == '1'

    # Test case passed
    sys.exit(0)

except Exception as e:
    # Capture screenshot if any exception happens
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\failure_screenshot.png")
    print(e)
    sys.exit(1)

finally:
    # Always close the driver
    driver.quit()
