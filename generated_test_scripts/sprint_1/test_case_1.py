
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Helper function to wait before every action
def wait_for_action():
    time.sleep(3)

# Configure chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-features=NetworkService")

# Initialize the driver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Navigate to the URL
    driver.get("https://saucedemo.com/")
    driver.maximize_window()
    time.sleep(5)  # Wait for 5 secs after opening the page

    # Login process
    from LoginPage import login  # Assuming LoginPage class exists and is correctly implemented
    login(driver, "standard_user", "secret_sauce")

    # Add 'Bike Light' to the cart
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
    wait_for_action()

    # Add 'Fleece Jacket' to the cart
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]'))).click()
    wait_for_action()

    # Verify cart badge displays '2'
    cart_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))).text
    if cart_count != '2':
        raise Exception('Cart badge count is incorrect. Expected 2, but got {}'.format(cart_count))

    # Remove 'Bike Light'
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]'))).click()
    wait_for_action()

    # Remove 'Fleece Jacket'
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]'))).click()
    wait_for_action()

    # Verify cart count element doesn't exist
    if WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))):
        pass
    else:
        raise Exception('Cart count element still exists')

    # Add 'Bolt T-Shirt' to the cart
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
    wait_for_action()

    # Verify cart badge displays '1'
    cart_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))).text
    if cart_count != '1':
        raise Exception('Cart badge count is incorrect. Expected 1, but got {}'.format(cart_count))

    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
    sys.exit(0)

except Exception as e:
    print(str(e))
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error_screenshot.png")
    sys.exit(1)
finally:
    driver.quit()
