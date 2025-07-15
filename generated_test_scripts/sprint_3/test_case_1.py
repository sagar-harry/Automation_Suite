
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import sys

def test_purchase_flow():
    url = "https://saucedemo.com/"
    username = "standard"
    password = "secret_sauce"

    options = Options()
    options.add_argument('--incognito')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--disable-features=NetworkService')

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(url)
    time.sleep(5)

    try:
        # Login Process
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='user-name']"))).send_keys(username)
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='login-button']").click()
        
        # Add items to the cart
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))).click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
        time.sleep(3)
        
        # Checkout Process
        driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@id='checkout']").click()
        
        # Enter Checkout Information
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='first-name']"))).send_keys("Jonnathan")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys("K")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys("10007")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='continue']").click()
        time.sleep(3)
        
        # Finish Purchase
        driver.find_element(By.XPATH, "//button[@id='finish']").click()
        time.sleep(3)
        
        # Return to homepage
        driver.find_element(By.XPATH, "//button[@id='back-to-products']").click()
        
        # Logout
        driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@id='logout_sidebar_link']"))).click()
        time.sleep(3)
        
        sys.exit(0)

    except (TimeoutException, NoSuchElementException) as e:
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots")
        sys.exit(1)
    finally:
        driver.quit()

test_purchase_flow()
