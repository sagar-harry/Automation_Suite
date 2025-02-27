
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

def wait_for_element(driver, by, locator, timeout=10):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            element = driver.find_element(by, locator)
            if element:
                return element
        except:
            time.sleep(0.5)
    raise Exception(f"Element with locator {locator} not found.")

try:
    # Set Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popups")
    chrome_options.add_argument("--disable-features=NetworkService")

    # Initialize the driver
    driver = webdriver.Chrome(options=chrome_options)
    
    # Open the website
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    driver.maximize_window()

    # Login
    login_username = wait_for_element(driver, By.XPATH, '//*[@id="user-name"]')
    login_username.send_keys("standard_user")
    time.sleep(3)
    
    login_password = wait_for_element(driver, By.XPATH, '//*[@id="password"]')
    login_password.send_keys("secret_sauce")
    time.sleep(3)
    
    login_button = wait_for_element(driver, By.XPATH, '//*[@id="login-button"]')
    login_button.click()
    time.sleep(3)

    # Add products to the cart
    bike_light = wait_for_element(driver, By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
    bike_light.click()
    time.sleep(3)
    
    fleece_jacket = wait_for_element(driver, By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
    fleece_jacket.click()
    time.sleep(3)
    
    # Proceed to checkout
    cart_icon = wait_for_element(driver, By.XPATH, '//*[@id="shopping_cart_container"]/a')
    cart_icon.click()
    time.sleep(3)
    
    checkout_button = wait_for_element(driver, By.XPATH, '//*[@id="checkout"]')
    checkout_button.click()
    time.sleep(3)
    
    first_name = wait_for_element(driver, By.XPATH, '//*[@id="first-name"]')
    first_name.send_keys("somename")
    time.sleep(3)
    
    last_name = wait_for_element(driver, By.XPATH, '//*[@id="last-name"]')
    last_name.send_keys("lastname")
    time.sleep(3)
    
    postal_code = wait_for_element(driver, By.XPATH, '//*[@id="postal-code"]')
    postal_code.send_keys("123456")
    time.sleep(3)
    
    continue_button = wait_for_element(driver, By.XPATH, '//*[@id="continue"]')
    continue_button.click()
    time.sleep(3)

    # Complete the purchase
    finish_button = wait_for_element(driver, By.XPATH, '//*[@id="finish"]')
    finish_button.click()
    time.sleep(3)

    # Return to homepage and logout
    back_to_products = wait_for_element(driver, By.XPATH, '//*[@id="back-to-products"]')
    back_to_products.click()
    time.sleep(3)
    
    logout_sidebar = wait_for_element(driver, By.XPATH, '//*[@id="react-burger-menu-btn"]')
    logout_sidebar.click()
    time.sleep(3)
    
    logout_button = wait_for_element(driver, By.XPATH, '//*[@id="logout_sidebar_link"]')
    logout_button.click()
    time.sleep(3)

    # Capture a screenshot of the page
    driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png')

    driver.quit()
    sys.exit(0)
except Exception as e:
    driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error_screenshot.png')
    driver.quit()
    sys.exit(1)
