
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def initialize_driver():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=NetworkService")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver

def login(driver):
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user"]'))).send_keys("standard")
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys("secret_sauce")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login-button"]'))).click()
    time.sleep(3)

def add_items_to_cart(driver):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="123"]/a'))).click()
    time.sleep(3)

def checkout(driver):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout"]'))).click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]'))).send_keys("Jonnathan")
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="last-name"]'))).send_keys("K")
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="postal-code"]'))).send_keys("10007")
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="continue"]'))).click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="finish"]'))).click()
    time.sleep(3)

def logout(driver):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-burger-menu-btn"]'))).click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="logout_sidebar_link"]'))).click()
    time.sleep(3)

def main():
    driver = None
    try:
        driver = initialize_driver()
        login(driver)
        add_items_to_cart(driver)
        checkout(driver)
        logout(driver)
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")
        sys.exit(0)
    except Exception as e:
        print(f"Test failed: {e}")
        if driver:
            driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error.png")
        sys.exit(1)
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    main()
