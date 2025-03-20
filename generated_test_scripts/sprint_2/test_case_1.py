
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

try:
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    # Open the website
    driver.get('https://saucedemo.com/')
    time.sleep(5)

    wait = WebDriverWait(driver, 10)

    # Login
    username = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]')))
    password = driver.find_element(By.XPATH, '//*[@id="password"]')
    login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    
    username.send_keys('standard_user')
    password.send_keys('secret_sauce')
    login_button.click()

    time.sleep(3)

    # Add items to cart
    bike_light = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
    bike_light.click()
    time.sleep(3)

    fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
    fleece_jacket.click()
    time.sleep(3)

    # Go to cart
    cart_icon = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a')))
    cart_icon.click()
    time.sleep(3)

    # Proceed to checkout
    checkout = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="checkout"]')))
    checkout.click()
    time.sleep(3)

    # Enter user information
    first_name = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="first-name"]')))
    last_name = driver.find_element(By.XPATH, '//*[@id="last-name"]')
    postal_code = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
    
    first_name.send_keys('Jonnathan')
    last_name.send_keys('K')
    postal_code.send_keys('10007')
    time.sleep(3)
    
    # Continue to complete purchase
    continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
    continue_button.click()
    time.sleep(3)

    finish_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="finish"]')))
    finish_button.click()
    time.sleep(3)

    # Return to products page
    back_to_products = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="back-to-products"]')))
    back_to_products.click()
    time.sleep(3)
    
    # Logout
    logout_sidebar = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-burger-menu-btn"]')))
    logout_sidebar.click()
    time.sleep(3)
    
    logout_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="logout_sidebar_link"]')))
    logout_button.click()
    
    time.sleep(3)

    # Screenshot
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")

    driver.quit()
    sys.exit(0)

except Exception as e:
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")
    driver.quit()
    sys.exit(1)
