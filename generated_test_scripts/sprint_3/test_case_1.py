
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# Initialize WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--disable-notifications")
options.add_argument("--disable-features=NetworkService")

driver = webdriver.Chrome(options=options)
driver.maximize_window()

try:
    driver.get("https://saucedemo.com/")
    time.sleep(5)

    # Login Process
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user"]')))
    driver.find_element(By.XPATH, '//*[@id="user"]').send_keys("standard")

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]')))
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")

    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

    # Add Items to Cart
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()

    # Proceed to Checkout
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="123"]/a')))
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="123"]/a').click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout"]')))
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()

    # Enter Checkout Information
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]')))
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("Jonnathan")

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="last-name"]')))
    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("K")

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="postal-code"]')))
    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("10007")

    # Complete Purchase
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="continue"]')))
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="finish"]')))
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="finish"]').click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="back-to-products"]')))
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()

    # Log Out
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-burger-menu-btn"]')))
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="logout_sidebar_link"]')))
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()

    # Save screenshot
    driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\result.png')

    sys.exit(0)
except Exception as e:
    driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error.png')
    sys.exit(1)
finally:
    driver.quit()
