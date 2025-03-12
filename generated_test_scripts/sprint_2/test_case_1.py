
import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import traceback

# Setup Chrome options
options = Options()
options.add_argument("--incognito")
options.add_argument("--disable-notifications")
options.add_argument("--disable-features=NetworkService")

try:
    # Initialize driver
    driver = webdriver.Chrome(options=options)
    
    # Open the login page
    driver.get("https://saucedemo.com/")
    sleep(5)  # Wait for the page to load
    driver.maximize_window()
    
    # Login using provided user credentials
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    sleep(3)
    
    # Add 'Bike Light' to cart
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    sleep(3)

    # Add 'Fleece Jacket' to cart
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    sleep(3)

    # Click on the cart icon
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    sleep(3)

    # Proceed to checkout
    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
    sleep(3)

    # Enter checkout information
    driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("Jonnathan")
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("K")
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("10007")
    sleep(3)

    # Continue and complete the purchase
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="finish"]').click()
    sleep(3)

    # Click finish button to return to homepage
    driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()
    sleep(3)

    # Logout from the account
    driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()
    sleep(3)

    # Test case passed, save screenshot and exit
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
    sys.exit(0)

except Exception as e:
    # Print stack trace if any exception occurs
    traceback.print_exc()
    # Save a screenshot for diagnosis
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\failure_screenshot.png")
    sys.exit(1)

finally:
    # Close the driver
    driver.quit()
