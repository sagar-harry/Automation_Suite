
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def create_webdriver():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=options)
    return driver

try:
    driver = create_webdriver()
    driver.maximize_window()
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="user-name"]'))).send_keys("standard_user")
    time.sleep(3)
    
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]'))).send_keys("secret_sauce")
    time.sleep(3)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]'))).click()
    time.sleep(5)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
    time.sleep(3)
    
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
    time.sleep(3)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]/a'))).click()
    time.sleep(3)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout"]'))).click()
    time.sleep(3)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="first-name"]'))).send_keys("Jonnathan")
    time.sleep(3)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="last-name"]'))).send_keys("K")
    time.sleep(3)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="postal-code"]'))).send_keys("10007")
    time.sleep(3)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="continue"]'))).click()
    time.sleep(3)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="finish"]'))).click()
    time.sleep(3)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="back-to-products"]'))).click()
    time.sleep(3)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="react-burger-menu-btn"]'))).click()
    time.sleep(3)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="logout_sidebar_link"]'))).click()
    time.sleep(3)

    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\completed_test.png")
    sys.exit(0)

except Exception as e:
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error.png")
    print("Exception occurred:", e)
    sys.exit(1)
finally:
    driver.quit()
