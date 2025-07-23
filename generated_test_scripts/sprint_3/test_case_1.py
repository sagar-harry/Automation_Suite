
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

try:
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=NetworkService")

    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://saucedemo.com/")
    time.sleep(5)

    # Wait for elements to be available
    wait = WebDriverWait(driver, 10)
    
    # Login
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='user-name']"))).send_keys("standard")
    time.sleep(3)
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))).send_keys("secret_sauce")
    time.sleep(3)
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='login-button']"))).click()
    time.sleep(3)

    # Add to cart
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))).click()
    time.sleep(3)
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"))).click()
    time.sleep(3)

    # Proceed to checkout
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='shopping_cart_link']"))).click()
    time.sleep(3)
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='checkout']"))).click()
    time.sleep(3)

    # Enter information
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='first-name']"))).send_keys("Jonnathan")
    time.sleep(3)
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='last-name']"))).send_keys("K")
    time.sleep(3)
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='postal-code']"))).send_keys("10007")
    time.sleep(3)
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='continue']"))).click()
    time.sleep(3)

    # Finish purchase
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='finish']"))).click()
    time.sleep(3)
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='back-to-products']"))).click()
    time.sleep(3)
    
    # Logout
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='react-burger-menu-btn']"))).click()
    time.sleep(3)
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='logout_sidebar_link']"))).click()

    # Save screenshot before closing
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")

    driver.quit()
    sys.exit(0)

except Exception as e:
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")
    driver.quit()
    sys.exit(1)
