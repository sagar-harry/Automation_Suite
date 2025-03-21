
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# Create Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-features=NetworkService")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Maximize window and navigate to the URL
    driver.maximize_window()
    driver.get("https://saucedemo.com/")
    time.sleep(5)

    # Log in using LoginPage method with predefined username and password
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(3)

    # Add 'Bike Light' and 'Fleece Jacket' to the cart
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]'))).click()
    time.sleep(3)

    # Assert cart count is '2'
    cart_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
    assert cart_count.text == "2"

    # Remove 'Bike Light' and 'Fleece Jacket'
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]'))).click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]'))).click()
    time.sleep(3)

    # Verify cart count element does not exist
    cart_count_elements = driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    assert len(cart_count_elements) == 0

    # Add 'Bolt T-Shirt' to the cart
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
    time.sleep(3)

    # Assert cart count is '1'
    cart_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
    assert cart_count.text == "1"

    # Take a screenshot in case of success
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\test_success.png")
    sys.exit(0)

except Exception as e:
    # Take a screenshot in case of failure
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\test_failure.png")
    sys.exit(1)

finally:
    driver.quit()
