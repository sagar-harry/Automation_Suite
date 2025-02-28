
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import sys

try:
    # Set up Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-features=NetworkService")
    
    driver = webdriver.Chrome(options=chrome_options)

    # Open the website
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    driver.maximize_window()

    # Login
    username = driver.find_element(By.XPATH, '//*[@id="user-name"]')
    username.send_keys("standard_user")
    time.sleep(3)

    password = driver.find_element(By.XPATH, '//*[@id="password"]')
    password.send_keys("secret_sauce")
    time.sleep(3)

    login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    login_button.click()
    time.sleep(3)

    # Add 'Bike Light' and 'Fleece Jacket' to the cart
    bike_light = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
    bike_light.click()
    time.sleep(3)

    fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
    fleece_jacket.click()
    time.sleep(3)

    # Proceed to checkout
    cart_icon = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    cart_icon.click()
    time.sleep(3)

    checkout = driver.find_element(By.XPATH, '//*[@id="checkout"]')
    checkout.click()
    time.sleep(3)

    # Enter checkout information
    first_name = driver.find_element(By.XPATH, '//*[@id="first-name"]')
    first_name.send_keys("Jonnathan")
    time.sleep(3)

    last_name = driver.find_element(By.XPATH, '//*[@id="last-name"]')
    last_name.send_keys("K")
    time.sleep(3)

    postal_code = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
    postal_code.send_keys("10007")
    time.sleep(3)

    continue_checkout = driver.find_element(By.XPATH, '//*[@id="continue"]')
    continue_checkout.click()
    time.sleep(3)

    finish = driver.find_element(By.XPATH, '//*[@id="finish"]')
    finish.click()
    time.sleep(3)

    # Return to homepage
    back_to_products = driver.find_element(By.XPATH, '//*[@id="back-to-products"]')
    back_to_products.click()
    time.sleep(3)

    # Logout
    logout_sidebar = driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]')
    logout_sidebar.click()
    time.sleep(3)

    logout_button = driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]')
    logout_button.click()
    time.sleep(3)

    # Save snapshot
    driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\last_page.png')

    sys.exit(0)

except Exception as e:
    print(f"An error occurred: {e}")
    driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error_page.png')
    sys.exit(1)

finally:
    driver.quit()
