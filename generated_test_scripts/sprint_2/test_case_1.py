
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def take_screenshot(driver):
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\test_case_screenshot.png")

try:
    # Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-features=NetworkService")

    # Initialize Chrome driver
    driver = webdriver.Chrome(options=chrome_options)

    # Open URL
    driver.get("https://saucedemo.com/")
    time.sleep(5)  # Wait for 5 seconds

    # Maximize the window
    driver.maximize_window()

    # Create WebDriverWait object
    wait = WebDriverWait(driver, 10)

    # Login
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))).send_keys("standard_user")
    time.sleep(3)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys("secret_sauce")
    time.sleep(3)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login-button"]'))).click()
    time.sleep(3)

    # Add items to cart
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
    time.sleep(3)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
    time.sleep(3)

    # Click on cart icon
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a'))).click()
    time.sleep(3)

    # Proceed to checkout
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout"]'))).click()
    time.sleep(3)

    # Fill checkout information
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]'))).send_keys("Jonnathan")
    time.sleep(3)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="last-name"]'))).send_keys("K")
    time.sleep(3)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="postal-code"]'))).send_keys("10007")
    time.sleep(3)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="continue"]'))).click()
    time.sleep(3)

    # Finish purchase
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="finish"]'))).click()
    time.sleep(3)

    # Return to homepage
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="back-to-products"]'))).click()
    time.sleep(3)

    # Logout
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-burger-menu-btn"]'))).click()
    time.sleep(3)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="logout_sidebar_link"]'))).click()

    # Take screenshot and exit with success
    take_screenshot(driver)
    sys.exit(0)

except Exception as e:
    print(f"Test failed: {e}")
    sys.exit(1)

finally:
    driver.quit()
