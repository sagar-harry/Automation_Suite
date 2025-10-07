
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

try:
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)
    driver.get("https://saucedemo.com/")
    driver.maximize_window()
    time.sleep(5)

    # Wait 3 seconds before each action
    login_wait = WebDriverWait(driver, 10)
    username = login_wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='user-name']")))
    password = driver.find_element(By.XPATH, "//input[@id='password']")
    login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")

    username.send_keys("standard")
    time.sleep(3)
    password.send_keys("secret_sauce")
    time.sleep(3)
    login_button.click()

    # Add Bike Light and Fleece Jacket to the cart
    bike_light_button = login_wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")))
    bike_light_button.click()
    time.sleep(3)

    fleece_jacket_button = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
    fleece_jacket_button.click()
    time.sleep(3)

    # Proceed to Cart
    cart_icon = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
    cart_icon.click()
    time.sleep(3)

    # Proceed to Checkout
    checkout_button = login_wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='checkout']")))
    checkout_button.click()
    time.sleep(3)

    # Enter user information
    first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
    last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
    zip_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")

    first_name.send_keys("Jonnathan")
    time.sleep(3)
    last_name.send_keys("K")
    time.sleep(3)
    zip_code.send_keys("10007")
    time.sleep(3)

    continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
    continue_button.click()
    time.sleep(3)

    # Finish purchase
    finish_button = login_wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='finish']")))
    finish_button.click()
    time.sleep(3)

    # Return to homepage
    back_to_products_button = driver.find_element(By.XPATH, "//button[@id='back-to-products']")
    back_to_products_button.click()
    time.sleep(3)

    # Logout
    menu_button = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
    menu_button.click()
    time.sleep(3)
    
    logout_link = login_wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@id='logout_sidebar_link']")))
    logout_link.click()

    # Take a screenshot before closing
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
    driver.quit()
    sys.exit(0)

except Exception as e:
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error_screenshot.png")
    driver.quit()
    sys.exit(1)
