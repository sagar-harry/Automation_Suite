
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-features=NetworkService")

try:
    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    # Go to login page
    driver.get("https://www.saucedemo.com/")
    time.sleep(5)

    # Wait for username to be present and enter credentials
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]')))
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

    # Add items to cart
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(3)

    # Proceed to checkout
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
    time.sleep(3)

    # Enter checkout information
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="first-name"]')))
    driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("Janathan")
    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("K")
    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("10007")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()
    time.sleep(3)

    # Finish purchase
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="finish"]')))
    driver.find_element(By.XPATH, '//*[@id="finish"]').click()
    time.sleep(3)

    # Take screenshot
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\after_purchase.png")

    # Logout
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-burger-menu-btn"]')))
    driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="logout_sidebar_link"]')))
    driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()
    time.sleep(3)

    driver.quit()
    sys.exit(0)

except Exception as e:
    driver.quit()
    print(f"Test failed: {e}")
    sys.exit(1)
