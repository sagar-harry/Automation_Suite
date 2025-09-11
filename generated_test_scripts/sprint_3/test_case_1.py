
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys

try:
    # Configure WebDriver options
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-features=NetworkService")
    driver = webdriver.Chrome(options=options)

    # Open URL
    driver.get("https://saucedemo.com/")
    time.sleep(5)  # Wait for the page to load
    driver.maximize_window()

    # Login to the application
    def login(username, password):
        user_field = driver.find_element(By.XPATH, "//input[@id='user-name']")
        user_field.send_keys(username)
        time.sleep(3)
        password_field = driver.find_element(By.XPATH, "//input[@id='password']")
        password_field.send_keys(password)
        time.sleep(3)
        login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
        login_button.click()
        time.sleep(3)

    login("standard", "secret_sauce")

    # Add 'Bike Light' and 'Fleece Jacket' to the cart
    bike_light_button = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
    fleece_jacket_button = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
    bike_light_button.click()
    time.sleep(3)
    fleece_jacket_button.click()
    time.sleep(3)

    # Click on cart icon
    cart_icon = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
    cart_icon.click()
    time.sleep(3)

    # Proceed to checkout
    checkout_button = driver.find_element(By.XPATH, "//button[@id='checkout']")
    checkout_button.click()
    time.sleep(3)

    # Enter checkout information
    first_name_field = driver.find_element(By.XPATH, "//input[@id='first-name']")
    first_name_field.send_keys("Jonnathan")
    time.sleep(3)
    last_name_field = driver.find_element(By.XPATH, "//input[@id='last-name']")
    last_name_field.send_keys("K")
    time.sleep(3)
    zip_code_field = driver.find_element(By.XPATH, "//input[@id='postal-code']")
    zip_code_field.send_keys("10007")
    time.sleep(3)

    # Continue and complete the purchase
    continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
    continue_button.click()
    time.sleep(3)
    finish_button = driver.find_element(By.XPATH, "//button[@id='finish']")
    finish_button.click()
    time.sleep(3)

    # Return to homepage
    back_home_button = driver.find_element(By.XPATH, "//button[@id='back-to-products']")
    back_home_button.click()
    time.sleep(3)

    # Logout of the application
    menu_button = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
    menu_button.click()
    time.sleep(3)
    logout_link = driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']")
    logout_link.click()
    time.sleep(3)

    # Test passed
    sys.exit(0)

except Exception as e:
    # Capture screenshot if test fails
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\failure.png")
    # Test failed
    sys.exit(1)

finally:
    driver.quit()
