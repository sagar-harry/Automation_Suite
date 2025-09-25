
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time
import os

try:
    # Set up Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=NetworkService")

    # Initialize WebDriver
    driver = webdriver.Chrome(options=options)

    # Open the website and configure settings
    driver.get("https://saucedemo.com/")
    driver.maximize_window()
    time.sleep(5)

    # Login to the site
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='user-name']"))
    ).send_keys("standard_user")
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))
    ).send_keys("secret_sauce")
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='login-button']"))
    ).click()
    time.sleep(3)

    # Add items to the cart
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))
    ).click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"))
    ).click()
    time.sleep(3)

    # Proceed to checkout
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@class='shopping_cart_link']"))
    ).click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@id='checkout']"))
    ).click()
    time.sleep(3)

    # Enter checkout information
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='first-name']"))
    ).send_keys("Jonnathan")
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='last-name']"))
    ).send_keys("K")
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='postal-code']"))
    ).send_keys("10007")
    time.sleep(3)

    # Continue to payment
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='continue']"))
    ).click()
    time.sleep(3)

    # Verify if 'Payment Information' label is visible
    payment_label_visible = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='Payment Information']"))
    )

    if payment_label_visible:
        screenshot_dir = "C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        driver.save_screenshot(os.path.join(screenshot_dir, "payment_information_visible.png"))
        sys.exit(0)
    else:
        sys.exit(1)

except Exception as e:
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\failure.png")
    sys.exit(1)
finally:
    driver.quit()
