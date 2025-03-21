
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import os

options = Options()
options.add_argument("--incognito")
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-features=NetworkService")

driver = webdriver.Chrome(options=options)
driver.get("https://saucedemo.com/")
time.sleep(5)
driver.maximize_window()

try:
    # Login Test
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user"]')))
    driver.find_element(By.XPATH, '//*[@id="user"]').send_keys("standard")
    time.sleep(3)
    
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    time.sleep(3)
    
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(3)
    
    # Adding items to cart
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(3)

    # Checkout process
    driver.find_element(By.XPATH, '//*[@id="123"]/a').click()
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
    time.sleep(3)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="first-name"]')))
    driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("Jonnathan")
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("K")
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("10007")
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="continue"]').click()
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="finish"]').click()
    time.sleep(3)

    # Verify back to products
    driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()
    time.sleep(3)

    # Logout
    driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
    time.sleep(3)
    
    driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()
    time.sleep(3)

    # Save the snapshot of the page
    screenshot_path = "C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots"
    os.makedirs(screenshot_path, exist_ok=True)
    full_screenshot_path = os.path.join(screenshot_path, "screenshot.png")
    driver.save_screenshot(full_screenshot_path)

    driver.quit()
    sys.exit(0)
except Exception as e:
    print(f"Test failed: {e}")
    driver.quit()
    sys.exit(1)
