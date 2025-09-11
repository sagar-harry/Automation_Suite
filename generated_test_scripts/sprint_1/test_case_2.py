
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def login(driver):
    driver.get("https://saucedemo.com/")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "login-button"))).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "inventory_container")))

def run_test():
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")
    
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    try:
        login(driver)

        driver.get("https://saucedemo.com/")
        WebDriverWait(driver, 3)

        # Add 'Bike Light' to cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bike-light"))).click()
        WebDriverWait(driver, 3)

        # Add 'Fleece Jacket' to cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-fleece-jacket"))).click()
        WebDriverWait(driver, 3)

        # Proceed to checkout
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
        WebDriverWait(driver, 3)

        # Fill in checkout information
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Jonnathan")
        WebDriverWait(driver, 3)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "last-name"))).send_keys("K")
        WebDriverWait(driver, 3)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "postal-code"))).send_keys("10007")
        WebDriverWait(driver, 3)

        # Continue to payment
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "continue"))).click()
        WebDriverWait(driver, 3)

        # Verify 'Payment Information'
        payment_info = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Payment Information']")))
        
        if payment_info.is_displayed():
            driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
            sys.exit(0)
        else:
            sys.exit(1)

    except Exception as e:
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
        sys.exit(1)
    finally:
        driver.quit()

run_test()
