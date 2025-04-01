
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure Chrome Options
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-features=NetworkService")

try:
    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the website
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    driver.maximize_window()

    # Wait for elements and perform login
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user"]')))
    driver.find_element(By.XPATH, '//*[@id="user"]').send_keys("standard")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(3)

    # Add items to the cart
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(3)

    # Proceed to checkout
    driver.find_element(By.XPATH, '//*[@id="123"]/a').click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout"]')))
    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
    time.sleep(3)

    # Enter shipping details
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]')))
    driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("Jonnathan")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("K")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("10007")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()
    time.sleep(3)

    # Complete the purchase
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="finish"]')))
    driver.find_element(By.XPATH, '//*[@id="finish"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()
    time.sleep(3)

    # Logout
    driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="logout_sidebar_link"]')))
    driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()
    time.sleep(3)

    # Capture screenshot
    driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png')

    # Exit script with success
    driver.quit()
    sys.exit(0)

except Exception as e:
    # Capture screenshot on failure
    driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot_error.png')
    driver.quit()
    print(f"Test failed due to {e}")
    sys.exit(1)
