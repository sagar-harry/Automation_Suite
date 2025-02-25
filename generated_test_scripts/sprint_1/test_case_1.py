
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

# Initialize Chrome options
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-notifications')
options.add_argument('--incognito')
options.add_argument('--disable-features=NetworkService')

# Initialize driver
driver = webdriver.Chrome(options=options)

# Maximize window
driver.maximize_window()

# Define the wait time
wait_time = 5

try:
    # Open the website
    driver.get("https://saucedemo.com/")
    time.sleep(wait_time)

    # Locate and interact with login elements
    username_input = WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))
    )
    password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
    login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')

    # Login
    username_input.send_keys("standard_user")
    time.sleep(wait_time / 2)
    password_input.send_keys("secret_sauce")
    time.sleep(wait_time / 2)
    login_button.click()
    time.sleep(wait_time)

    # Add 'Bike Light' and 'Fleece Jacket' to the cart
    bike_light = WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
    )
    fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')

    bike_light.click()
    time.sleep(wait_time)
    fleece_jacket.click()
    time.sleep(wait_time)

    # Verify cart badge displays '2'
    cart_count = WebDriverWait(driver, wait_time).until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'), '2')
    )

    # Remove 'Bike Light' and 'Fleece Jacket'
    remove_bike_light = driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]')
    remove_fleece_jacket = driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]')

    remove_bike_light.click()
    time.sleep(wait_time)
    remove_fleece_jacket.click()
    time.sleep(wait_time)

    # Verify cart count element does not exist
    try:
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        sys.exit(1)
    except:
        pass

    # Add 'Bolt T-Shirt' to the cart
    add_bolt_tshirt = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
    add_bolt_tshirt.click()
    time.sleep(wait_time)

    # Verify cart badge displays '1'
    cart_count = WebDriverWait(driver, wait_time).until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'), '1')
    )

    # Test case passed
    sys.exit(0)

except Exception as e:
    print(f"Test case failed due to an exception: {e}")
    sys.exit(1)

finally:
    driver.quit()
