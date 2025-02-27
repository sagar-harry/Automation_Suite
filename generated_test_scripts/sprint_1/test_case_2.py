
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Chrome Options
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-features=NetworkService")

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Navigate to the website
    driver.get("https://saucedemo.com/")
    time.sleep(5)  # Wait for 5 seconds
    driver.maximize_window()

    # Perform login
    from LoginPage import login  # Assuming login method is implemented in LoginPage.py
    login(driver, "standard_user", "secret_sauce")

    time.sleep(3)  # Wait for 3 seconds

    # Add Bike Light to the cart
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
    time.sleep(3)

    # Add Fleece Jacket to the cart
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
    time.sleep(3)

    # Click on Cart icon
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]/a'))).click()
    time.sleep(3)

    # Click on Checkout
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout"]'))).click()
    time.sleep(3)

    # Enter First Name
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]'))).send_keys("somename")
    time.sleep(3)

    # Enter Last Name
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="last-name"]'))).send_keys("lastname")
    time.sleep(3)

    # Enter Zip Code
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="postal-code"]'))).send_keys("123456")
    time.sleep(3)

    # Click on Continue
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="continue"]'))).click()
    time.sleep(3)

    # Verify the 'Payment Information' label is visible
    payment_info_label = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]')))
    if payment_info_label:
        # Save the page snapshot
        driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png')
        sys.exit(0)  # Test case passed
    
except Exception as e:
    print(f"Test case failed: {str(e)}")
    driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png')
    sys.exit(1)  # Test case failed

finally:
    # Close the driver
    driver.quit()
