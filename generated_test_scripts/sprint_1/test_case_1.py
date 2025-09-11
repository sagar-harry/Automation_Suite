
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import sys
import traceback

options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--incognito")
options.add_argument("--disable-features=NetworkService")

def test_ui_scenario():
    try:
        driver = webdriver.Chrome(options=options)
        driver.get("https://saucedemo.com/")
        time.sleep(5)  # Wait for the page to load
        driver.maximize_window()

        # Page login
        driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
        driver.find_element(By.XPATH, "//input[@id='login-button']").click()
        time.sleep(3)

        # Add 'Bike Light' to the cart
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))
        ).click()
        time.sleep(3)

        # Add 'Fleece Jacket' to the cart
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"))
        ).click()
        time.sleep(3)

        # Check if cart count is 2
        cart_badge = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']"))
        )
        assert cart_badge.text == "2"

        # Remove 'Bike Light' from the cart
        driver.find_element(By.XPATH, "//button[@id='remove-sauce-labs-bike-light']").click()
        time.sleep(3)

        # Remove 'Fleece Jacket' from the cart
        driver.find_element(By.XPATH, "//button[@id='remove-sauce-labs-fleece-jacket']").click()
        time.sleep(3)

        # Verify cart badge does not exist
        assert not len(driver.find_elements(By.XPATH, "//span[@class='shopping_cart_badge']"))

        # Add 'Bolt T-Shirt' to the cart
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"))
        ).click()
        time.sleep(3)

        # Verify cart badge shows '1'
        cart_badge = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']"))
        )
        assert cart_badge.text == "1"

        sys.exit(0)

    except Exception as e:
        print(traceback.format_exc())
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\failure.png")
        sys.exit(1)

    finally:
        driver.quit()

test_ui_scenario()
