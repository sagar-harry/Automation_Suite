
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

def test_purchase_flow():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=NetworkService")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()

        # Login
        login_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='user-name']"))
        )
        passwd_input = driver.find_element(By.XPATH, "//input[@id='password']")
        login_btn = driver.find_element(By.XPATH, "//input[@id='login-button']")
        login_input.send_keys("standard")
        time.sleep(3)
        passwd_input.send_keys("secret_sauce")
        time.sleep(3)
        login_btn.click()

        # Add items to cart
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))
        ).click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
        time.sleep(3)
        
        # Proceed to checkout
        driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@id='checkout']"))
        ).click()
        time.sleep(3)
        
        # Fill delivery information
        first_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='first-name']"))
        )
        last_name_input = driver.find_element(By.XPATH, "//input[@id='last-name']")
        zip_code_input = driver.find_element(By.XPATH, "//input[@id='postal-code']")
        first_name_input.send_keys("Jonnathan")
        time.sleep(3)
        last_name_input.send_keys("K")
        time.sleep(3)
        zip_code_input.send_keys("10007")
        time.sleep(3)
        
        # Continue and complete purchase
        driver.find_element(By.XPATH, "//input[@id='continue']").click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@id='finish']"))
        ).click()
        time.sleep(3)

        # Return to homepage
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@id='back-to-products']"))
        ).click()
        time.sleep(3)

        # Logout process
        driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@id='logout_sidebar_link']"))
        ).click()
        time.sleep(3)

        # Save screenshot
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")

        # Test case passed
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    finally:
        driver.quit()

test_purchase_flow()
