
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def login(driver):
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

def logout(driver):
    driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
    time.sleep(3)  # Wait for animation
    driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()

def test_complete_purchase_flow():
    # Setup Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=NetworkService")

    try:
        # Initialize WebDriver
        driver = webdriver.Chrome(chrome_options=options)
        driver.maximize_window()
        driver.get("https://saucedemo.com/")
        time.sleep(5)  # Wait after opening page

        login(driver)

        # Wait for elements and perform actions
        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        ).click()

        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        ).click()

        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]/a'))
        ).click()

        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout"]'))
        ).click()

        # Enter checkout information
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('somename')
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('lastname')
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys('123456')
        
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="continue"]').click()

        # Finish purchase
        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="finish"]'))
        ).click()

        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="back-to-products"]'))
        )
        
        logout(driver)

        # Successful test
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\complete_purchase_flow.png")
        sys.exit(0)
        
    except Exception as e:
        print(f"Test failed: {e}")
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\failed_complete_purchase_flow.png")
        sys.exit(1)
    finally:
        driver.quit()

test_complete_purchase_flow()
