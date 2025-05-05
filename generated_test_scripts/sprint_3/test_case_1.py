
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# Initialize Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-features=NetworkService")

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open the website
    driver.get("https://saucedemo.com/")
    
    # Maximize the browser window
    driver.maximize_window()
    
    # Wait for 5 seconds
    time.sleep(5)
    
    # Login to the application
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="user"]'))
    ).send_keys("standard")
    time.sleep(3)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]'))
    ).send_keys("secret_sauce")
    time.sleep(3)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]'))
    ).click()
    time.sleep(3)
    
    # Add items to the cart
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
    ).click()
    time.sleep(3)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
    ).click()
    time.sleep(3)

    # Click on the cart icon
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="123"]/a'))
    ).click()
    time.sleep(3)

    # Proceed to checkout
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout"]'))
    ).click()
    time.sleep(3)

    # Enter user details
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="first-name"]'))
    ).send_keys("Jonnathan")
    time.sleep(3)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="last-name"]'))
    ).send_keys("K")
    time.sleep(3)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="postal-code"]'))
    ).send_keys("10007")
    time.sleep(3)

    # Click continue and finish purchase
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="continue"]'))
    ).click()
    time.sleep(3)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="finish"]'))
    ).click()
    time.sleep(3)

    # Return to homepage
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="back-to-products"]'))
    ).click()
    time.sleep(3)

    # Log out
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="react-burger-menu-btn"]'))
    ).click()
    time.sleep(3)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="logout_sidebar_link"]'))
    ).click()
    time.sleep(3)

    # Save screenshot
    driver.save_screenshot('C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png')

    # Exit with success
    sys.exit(0)

except Exception as e:
    driver.save_screenshot('C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error_screenshot.png')
    sys.exit(1)

finally:
    # Close the browser
    driver.quit()
