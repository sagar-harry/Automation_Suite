
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

try:
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-features=NetworkService")

    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    # Navigate to the login page
    driver.get('https://saucedemo.com')
    time.sleep(5)  # Wait after opening the page

    # Login
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user"]'))).send_keys('standard')
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys('secret_sauce')
    time.sleep(3)  # Wait before login
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]'))).click()

    # Add items to the cart
    time.sleep(3)  # Wait before adding items
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()

    # Go to cart
    time.sleep(3)  # Wait before clicking on cart icon
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="123"]/a'))).click()

    # Proceed to checkout
    time.sleep(3)  # Wait before checkout
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout"]'))).click()

    # Enter checkout information
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]'))).send_keys('Jonnathan')
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="last-name"]'))).send_keys('K')
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="postal-code"]'))).send_keys('10007')
    time.sleep(3)  # Wait before continue
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="continue"]'))).click()

    # Complete the purchase and return to homepage
    time.sleep(3)  # Wait before finish
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="finish"]'))).click()

    # Click Finish and go back to homepage
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="back-to-products"]'))).click()

    # Logout
    time.sleep(3)  # Wait before logout
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-burger-menu-btn"]'))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="logout_sidebar_link"]'))).click()

    # Screenshot
    time.sleep(3)  # Wait before taking screenshot
    driver.save_screenshot("C:/Users/Administrator/Desktop/QE_COE/automated_pipeline_2/captured_screenshots/screenshot.png")

    # Successful execution
    sys.exit(0)

except Exception as e:
    print(f"Test case failed: {e}")
    sys.exit(1)

finally:
    driver.quit()
