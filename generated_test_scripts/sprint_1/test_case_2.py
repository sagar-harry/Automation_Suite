
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

def initialize_driver():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get('https://saucedemo.com/')
    time.sleep(5)
    return driver

def login(driver, username, password):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))).send_keys(username)
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys(password)
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login-button"]'))).click()
    time.sleep(3)

def add_items_to_cart(driver):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
    time.sleep(3)

def checkout(driver):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a'))).click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout"]'))).click()
    time.sleep(3)

def enter_checkout_details(driver):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]'))).send_keys('Jonnathan')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="last-name"]'))).send_keys('K')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="postal-code"]'))).send_keys('10007')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="continue"]'))).click()
    time.sleep(3)

def verify_payment_information(driver):
    try:
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]'))).is_displayed()
        return True
    except Exception as e:
        return False

def capture_screenshot(driver, path):
    driver.save_screenshot(path)

def main():
    driver = initialize_driver()
    try:
        login(driver, 'standard_user', 'secret_sauce')
        add_items_to_cart(driver)
        checkout(driver)
        enter_checkout_details(driver)
        if verify_payment_information(driver):
            capture_screenshot(driver, "C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")
            sys.exit(0)
        else:
            capture_screenshot(driver, "C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\failed_screenshot.png")
            sys.exit(1)
    except Exception as e:
        capture_screenshot(driver, "C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error_screenshot.png")
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
