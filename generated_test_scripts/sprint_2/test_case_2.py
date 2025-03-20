
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popups")
chrome_options.add_argument("--disable-features=NetworkService")

# Initialize driver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open the website
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    driver.maximize_window()

    # Wait for elements to load and perform login action
    wait = WebDriverWait(driver, 10)
    username_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]')))
    password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
    login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')

    time.sleep(3)
    username_field.send_keys("standard_user")
    time.sleep(3)
    password_field.send_keys("secret_sauce")
    time.sleep(3)
    login_button.click()

    # Wait for and add items to cart
    bike_light = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
    fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')

    time.sleep(3)
    bike_light.click()
    time.sleep(3)
    fleece_jacket.click()

    # Verify cart count
    cart_count = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
    time.sleep(3)
    
    if cart_count.text == '2':
        # Test passed, take screenshot
        driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\test_passed.png')
        sys.exit(0)
    else:
        raise Exception("Cart count mismatch")

except Exception as e:
    driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\test_failed.png')
    sys.exit(1)

finally:
    driver.quit()
