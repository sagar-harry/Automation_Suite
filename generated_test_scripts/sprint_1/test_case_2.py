
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# Configuration
url = "https://saucedemo.com/"
username = "standard_user"
password = "secret_sauce"
screenshot_path = r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png"

# Setup
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--disable-notifications")
options.add_argument("--disable-features=NetworkService")

driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(5)
driver.maximize_window()

try:
    # Login
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']"))).send_keys(username)
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']"))).send_keys(password)
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']"))).click()
    time.sleep(3)

    # Add Bike Light to cart
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))).click()
    time.sleep(3)

    # Add Fleece Jacket to cart
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"))).click()
    time.sleep(3)

    # Proceed to Checkout
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='checkout']"))).click()
    time.sleep(3)

    # Enter Checkout details
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "firstName"))).send_keys("Jonnathan")
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "lastName"))).send_keys("K")
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "postalCode"))).send_keys("10007")
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='continue']"))).click()
    time.sleep(3)

    # Verify Payment Information is visible
    payment_info = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Payment Information')]")))
    time.sleep(3)

    # Capture screenshot
    driver.save_screenshot(screenshot_path)

    # Validation
    if payment_info:
        sys.exit(0)
    
except Exception as e:
    driver.save_screenshot(screenshot_path)
    sys.exit(1)

finally:
    driver.quit()
