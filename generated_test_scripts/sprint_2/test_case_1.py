
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import os

try:
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)
    driver.get("https://saucedemo.com/")

    time.sleep(5)  # Wait for 5 seconds after opening the page
    driver.maximize_window()

    # Login
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))
    ).send_keys("standard_user")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

    # Add 'Bike Light' to Cart
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
    ).click()
    time.sleep(3)

    # Add 'Fleece Jacket' to Cart
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(3)

    # Go to Cart
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    time.sleep(3)

    # Proceed to Checkout
    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
    time.sleep(3)

    # Enter Checkout Information
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="first-name"]'))
    ).send_keys("Jonnathan")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("K")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("10007")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()
    time.sleep(3)

    # Finish the purchase
    driver.find_element(By.XPATH, '//*[@id="finish"]').click()
    time.sleep(3)

    # Back to products
    driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()
    time.sleep(3)

    # Logout
    driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()
    time.sleep(3)

    # Capture Screenshot
    screenshot_path = r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\test_completed.png"
    os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
    driver.save_screenshot(screenshot_path)

    driver.quit()
    sys.exit(0)

except Exception as e:
    print(f"Test failed: {e}")
    driver.quit()
    sys.exit(1)
