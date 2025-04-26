
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import os

try:
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=NetworkService")
    driver = webdriver.Chrome(options=options)

    driver.get("https://saucedemo.com/")
    driver.maximize_window()
    time.sleep(5)

    wait = WebDriverWait(driver, 10)
    
    # Login
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user"]'))).send_keys("standard")
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys("secret_sauce")
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]'))).click()
    time.sleep(3)

    # Add items to cart
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
    time.sleep(3)

    # Go to cart and checkout
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="123"]/a'))).click()
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout"]'))).click()
    time.sleep(3)

    # Enter shipping information
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]'))).send_keys("Jonnathan")
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="last-name"]'))).send_keys("K")
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="postal-code"]'))).send_keys("10007")
    time.sleep(3)

    # Continue to purchase
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="continue"]'))).click()
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="finish"]'))).click()
    time.sleep(3)

    # Capture snapshot before logging out
    screenshot_path = r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\homepage.png"
    driver.save_screenshot(screenshot_path)

    # Logout
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-burger-menu-btn"]'))).click()
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="logout_sidebar_link"]'))).click()
    time.sleep(3)

    sys.exit(0)

except Exception as e:
    print("Test case failed due to: ", str(e))
    screenshot_path = r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error.png"
    driver.save_screenshot(screenshot_path)
    sys.exit(1)

finally:
    driver.quit()
