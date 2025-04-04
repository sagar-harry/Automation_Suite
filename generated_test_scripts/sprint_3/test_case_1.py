
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time
import os

try:
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-features=NetworkService")

    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the website
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    driver.maximize_window()

    # Define an explicit wait
    wait = WebDriverWait(driver, 20)

    # Login process
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="user"]'))).send_keys("standard")
    time.sleep(3)

    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys("secret_sauce")
    time.sleep(3)

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]'))).click()
    time.sleep(3)

    # Add 'Bike Light' to the cart
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
    time.sleep(3)

    # Add 'Fleece Jacket' to the cart
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
    time.sleep(3)

    # Click on the cart icon
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="123"]/a'))).click()
    time.sleep(3)

    # Proceed to checkout
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout"]'))).click()
    time.sleep(3)

    # Enter checkout information
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="first-name"]'))).send_keys("Jonnathan")
    time.sleep(3)

    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="last-name"]'))).send_keys("K")
    time.sleep(3)

    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="postal-code"]'))).send_keys("10007")
    time.sleep(3)

    # Continue and Complete the purchase
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="continue"]'))).click()
    time.sleep(3)

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="finish"]'))).click()
    time.sleep(3)

    # Return to homepage
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="back-to-products"]'))).click()
    time.sleep(3)

    # Logout process
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-burger-menu-btn"]'))).click()
    time.sleep(3)

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="logout_sidebar_link"]'))).click()
    time.sleep(3)

    # Test case success, take a screenshot
    screenshot_directory = r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots"
    os.makedirs(screenshot_directory, exist_ok=True)
    driver.save_screenshot(os.path.join(screenshot_directory, "completed_test.png"))

    sys.exit(0)
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)
finally:
    # Close the webdriver
    driver.quit()
