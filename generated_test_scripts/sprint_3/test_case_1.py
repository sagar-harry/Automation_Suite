
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popups")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)

    driver.get("https://saucedemo.com/")
    driver.maximize_window()
    time.sleep(5)

    # Login
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='user-name']"))
    ).send_keys("standard")

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='password']"))
    ).send_keys("secret_sauce")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']"))
    ).click()
    time.sleep(3)

    # Add 'Bike Light' and 'Fleece Jacket' to the cart
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))
    ).click()
    time.sleep(3)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"))
    ).click()
    time.sleep(3)

    # Click on the Cart Icon
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='shopping_cart_link']"))
    ).click()
    time.sleep(3)

    # Proceed to Checkout
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='checkout']"))
    ).click()
    time.sleep(3)

    # Enter Checkout Information
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='first-name']"))
    ).send_keys("Jonnathan")

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='last-name']"))
    ).send_keys("K")

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='postal-code']"))
    ).send_keys("10007")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='continue']"))
    ).click()
    time.sleep(3)

    # Complete Purchase
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='finish']"))
    ).click()
    time.sleep(3)

    # Return to Homepage
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='back-to-products']"))
    ).click()
    time.sleep(3)

    # Logout
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='react-burger-menu-btn']"))
    ).click()
    time.sleep(3)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@id='logout_sidebar_link']"))
    ).click()
    time.sleep(3)

    sys.exit(0)

except Exception as e:
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")
    sys.exit(1)

finally:
    driver.quit()
