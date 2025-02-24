
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

def test_cart_count():
    url = 'https://saucedemo.com/'
    username = 'standard_user'
    password = 'secret_sauce'

    # Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--disable-features=NetworkService')

    # Initialize the webdriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Open the URL
        driver.get(url)
        time.sleep(5)  # Wait for 5 seconds after opening the page
        driver.maximize_window()

        # Wait for username field to appear and perform login
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]')))
        driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

        # Add 'Bike Light' to the cart
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)

        # Add 'Fleece Jacket' to the cart
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)

        # Verify cart badge displays '2'
        cart_count_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        cart_count = cart_count_element.text

        if cart_count == '2':
            sys.exit(0)
        else:
            sys.exit(1)

    except Exception as e:
        sys.exit(1)
    finally:
        driver.quit()

test_cart_count()
