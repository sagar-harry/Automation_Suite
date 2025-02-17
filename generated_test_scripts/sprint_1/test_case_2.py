
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import sys

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--incognito")

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Navigate to website
    driver.get('https://saucedemo.com/')
    time.sleep(5)  # Wait for 5 seconds after opening the page
    driver.maximize_window()

    # Login to the site using LoginPage class
    def login(username, password):
        driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(3)

    login('standard_user', 'secret_sauce')

    # Add Bike Light and Fleece Jacket to the cart
    bike_light = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
    time.sleep(3)
    bike_light.click()
    time.sleep(3)
    fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
    time.sleep(3)
    fleece_jacket.click()
    time.sleep(3)

    # Proceed to cart and checkout
    cart_icon = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    time.sleep(3)
    cart_icon.click()
    time.sleep(3)
    checkout_button = driver.find_element(By.XPATH, '//*[@id="checkout"]')
    time.sleep(3)
    checkout_button.click()
    time.sleep(3)

    # Enter checkout information
    first_name_field = driver.find_element(By.XPATH, '//*[@id="first-name"]')
    time.sleep(3)
    first_name_field.send_keys('somename')
    time.sleep(3)
    last_name_field = driver.find_element(By.XPATH, '//*[@id="last-name"]')
    last_name_field.send_keys('lastname')
    time.sleep(3)
    zip_code_field = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
    zip_code_field.send_keys('123456')
    time.sleep(3)

    # Continue to the next page
    continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
    time.sleep(3)
    continue_button.click()
    time.sleep(3)

    # Verify that Payment Information is visible
    payment_info_card = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]')
    if payment_info_card.is_displayed():
        print("Test Passed: 'Payment Information' label is visible")
        sys.exit(0)  # Exit with success code 0
    else:
        print("Test Failed: 'Payment Information' label is NOT visible")
        sys.exit(1)  # Exit with failure code 1

finally:
    driver.quit()
