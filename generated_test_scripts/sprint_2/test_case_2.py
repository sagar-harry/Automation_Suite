
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def test_add_items_to_cart():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=NetworkService")
    
    driver = webdriver.Chrome(options=options)

    try:
        driver.maximize_window()
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        wait = WebDriverWait(driver, 10)

        # Login
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))).send_keys("standard_user")
        time.sleep(3)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys("secret_sauce")
        time.sleep(3)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-button"]'))).click()
        time.sleep(3)

        # Add Bike Light to Cart
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
        time.sleep(3)

        # Add Fleece Jacket to Cart
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
        time.sleep(3)

        # Check Cart
        cart_badge = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        if cart_badge.text == "2":
            driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")
            sys.exit(0)
        else:
            driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot_failed.png")
            sys.exit(1)

    except Exception as e:
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot_exception.png")
        sys.exit(1)
    finally:
        driver.quit()

test_add_items_to_cart()
