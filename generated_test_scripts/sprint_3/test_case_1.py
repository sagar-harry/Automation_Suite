
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

# Configure options for Chrome
chrome_options = Options()
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument('--disable-features=NetworkService')

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open the website
    driver.get('https://saucedemo.com/')
    time.sleep(5)  # Waiting for the page to fully open
    driver.maximize_window()

    # Login process
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='user-name']"))).send_keys("standard")
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))).send_keys("secret_sauce")
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='login-button']"))).click()
    time.sleep(3)

    # Add 'Bike Light' and 'Fleece Jacket' to cart
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))).click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"))).click()
    time.sleep(3)

    # Go to cart and proceed to checkout
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='shopping_cart_link']"))).click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@id='checkout']"))).click()
    time.sleep(3)

    # Enter user details
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='first-name']"))).send_keys("Jonnathan")
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='last-name']"))).send_keys("K")
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='postal-code']"))).send_keys("10007")
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='continue']"))).click()
    time.sleep(3)

    # Complete purchase
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@id='finish']"))).click()
    time.sleep(3)

    # Return to homepage
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@id='back-to-products']")))

    # Logout process
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@id='react-burger-menu-btn']"))).click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@id='logout_sidebar_link']"))).click()
    time.sleep(3)

    # Save Screenshot
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")

    sys.exit(0)  # Test passed

except Exception as e:
    # Save Screenshot
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
    sys.exit(1)  # Test failed

finally:
    driver.quit()
