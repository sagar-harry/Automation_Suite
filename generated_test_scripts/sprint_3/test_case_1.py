
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

def wait_for_element(driver, by, value):
    for _ in range(10):
        try:
            element = driver.find_element(by, value)
            if element.is_displayed():
                return element
        except:
            pass
        time.sleep(1)
    raise Exception(f"Element not found: {value}")

try:
    # Setup Chrome options
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")

    # Initialize the Chrome driver
    driver = webdriver.Chrome(options=options)
    driver.get("https://saucedemo.com/")
    driver.maximize_window()
    time.sleep(5)

    # Login
    username_field = wait_for_element(driver, By.XPATH, "//input[@id='user-name']")
    username_field.send_keys("standard")
    time.sleep(3)
    
    password_field = wait_for_element(driver, By.XPATH, "//input[@id='password']")
    password_field.send_keys("secret_sauce")
    time.sleep(3)
    
    login_button = wait_for_element(driver, By.XPATH, "//input[@id='login-button']")
    login_button.click()
    time.sleep(3)

    # Add 'Bike Light' to cart
    bike_light_add_button = wait_for_element(driver, By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
    bike_light_add_button.click()
    time.sleep(3)

    # Add 'Fleece Jacket' to cart
    fleece_jacket_add_button = wait_for_element(driver, By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
    fleece_jacket_add_button.click()
    time.sleep(3)

    # Click on cart icon
    cart_icon = wait_for_element(driver, By.XPATH, "//a[@class='shopping_cart_link']")
    cart_icon.click()
    time.sleep(3)

    # Proceed to checkout
    checkout_button = wait_for_element(driver, By.XPATH, "//button[@id='checkout']")
    checkout_button.click()
    time.sleep(3)

    # Enter checkout information
    first_name_field = wait_for_element(driver, By.XPATH, "//input[@id='first-name']")
    first_name_field.send_keys("Jonnathan")
    time.sleep(3)

    last_name_field = wait_for_element(driver, By.XPATH, "//input[@id='last-name']")
    last_name_field.send_keys("K")
    time.sleep(3)

    postal_code_field = wait_for_element(driver, By.XPATH, "//input[@id='postal-code']")
    postal_code_field.send_keys("10007")
    time.sleep(3)

    continue_button = wait_for_element(driver, By.XPATH, "//input[@id='continue']")
    continue_button.click()
    time.sleep(3)

    # Complete the purchase
    finish_button = wait_for_element(driver, By.XPATH, "//button[@id='finish']")
    finish_button.click()
    time.sleep(3)

    # Click back to products/homepage
    back_to_products_button = wait_for_element(driver, By.XPATH, "//button[@id='back-to-products']")
    back_to_products_button.click()
    time.sleep(3)

    # Logout
    open_menu_button = wait_for_element(driver, By.XPATH, "//button[@id='react-burger-menu-btn']")
    open_menu_button.click()
    time.sleep(3)

    logout_link = wait_for_element(driver, By.XPATH, "//a[@id='logout_sidebar_link']")
    logout_link.click()
    time.sleep(3)

    driver.save_screenshot("C:/Users/Administrator/Desktop/QE_COE/automated_pipeline_2/captured_screenshots/screenshot.png")

    sys.exit(0)

except Exception as e:
    driver.save_screenshot("C:/Users/Administrator/Desktop/QE_COE/automated_pipeline_2/captured_screenshots/screenshot.png")
    print(e)
    sys.exit(1)

finally:
    driver.quit()
