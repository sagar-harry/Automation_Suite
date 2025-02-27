
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

try:
    chrome_options = Options()
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--disable-popup-blocking')
    chrome_options.add_argument('--disable-features=NetworkService')

    # Initialize driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://saucedemo.com/")
    time.sleep(5)  # Wait for 5 seconds before starting

    driver.maximize_window()

    # Log in
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))
    )
    password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
    login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    
    username_field.send_keys("standard_user")
    time.sleep(3)
    password_field.send_keys("secret_sauce")
    time.sleep(3)
    login_button.click()

    # Add items to cart
    bike_light = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
    )
    fleece_jacket = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
    )
    
    time.sleep(3)
    bike_light.click()
    time.sleep(3)
    fleece_jacket.click()

    # Proceed to cart and checkout
    cart_icon = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a'))
    )
    time.sleep(3)
    cart_icon.click()

    checkout_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="checkout"]'))
    )
    time.sleep(3)
    checkout_button.click()

    # Enter checkout information
    first_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="first-name"]'))
    )
    last_name = driver.find_element(By.XPATH, '//*[@id="last-name"]')
    postal_code = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
    
    first_name.send_keys("somename")
    time.sleep(3)
    last_name.send_keys("lastname")
    time.sleep(3)
    postal_code.send_keys("123456")
    
    continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
    time.sleep(3)
    continue_button.click()

    # Finish purchase
    finish_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="finish"]'))
    )
    time.sleep(3)
    finish_button.click()

    # Back to products and logout
    back_to_products = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="back-to-products"]'))
    )
    time.sleep(3)
    back_to_products.click()

    logout_sidebar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="react-burger-menu-btn"]'))
    )
    time.sleep(3)
    logout_sidebar.click()
    
    logout_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="logout_sidebar_link"]'))
    )
    time.sleep(3)
    logout_button.click()

    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\saucedemo.png")
    driver.quit()

    sys.exit(0)
except Exception as e:
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\saucedemo_error.png")
    driver.quit()
    sys.exit(1)
