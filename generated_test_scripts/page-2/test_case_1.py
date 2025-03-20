
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_add_items_to_cart():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--incognito")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()

        # Login
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))).send_keys("standard_user")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys("secret_sauce")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]'))).click()
        time.sleep(3)

        # Add Bike Light to cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
        time.sleep(3)

        # Add Fleece Jacket to cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
        time.sleep(3)

        # Verify cart badge displays '2'
        cart_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))).text
        assert cart_count == '2', f"Expected cart count to be 2 but got {cart_count}"

        # Take a screenshot
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")

        # Test passed
        sys.exit(0)

    except Exception as e:
        print(f"An error occurred: {e}")
        # Take a screenshot on failure
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\failed_screenshot.png")
        sys.exit(1)

    finally:
        driver.quit()

# Run the test case
test_add_items_to_cart()
