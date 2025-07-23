
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def login(driver):
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    driver.maximize_window()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='user-name']"))).send_keys("standard_user")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password']"))).send_keys("secret_sauce")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='login-button']"))).click()

def test_shopping_cart():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        login(driver)
        time.sleep(3)

        # Add 'Bike Light' to the cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))).click()
        time.sleep(3)

        # Add 'Fleece Jacket' to the cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"))).click()
        time.sleep(3)

        # Verify cart badge shows '2'
        cart_badge = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']")))
        assert cart_badge.text == '2'
        time.sleep(3)

        # Remove 'Bike Light'
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='remove-sauce-labs-bike-light']"))).click()
        time.sleep(3)

        # Remove 'Fleece Jacket'
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='remove-sauce-labs-fleece-jacket']"))).click()
        time.sleep(3)

        # Verify cart badge does not exist
        assert len(driver.find_elements(By.XPATH, "//span[@class='shopping_cart_badge']")) == 0
        time.sleep(3)

        # Add 'Bolt T-Shirt' to the cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"))).click()
        time.sleep(3)

        # Verify cart badge shows '1'
        cart_badge = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']")))
        assert cart_badge.text == '1'
        time.sleep(3)

        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\snapshot.png")
        sys.exit(0)
        
    except Exception as e:
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\snapshot.png")
        sys.exit(1)
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_shopping_cart()
