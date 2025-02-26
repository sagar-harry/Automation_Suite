
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def login(driver, username, password):
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    driver.maximize_window()
    
    wait = WebDriverWait(driver, 10)
    username_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='user-name']")))
    password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='password']")))
    login_button = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='login-button']")))
    
    username_field.send_keys(username)
    time.sleep(3)
    password_field.send_keys(password)
    time.sleep(3)
    login_button.click()

def test_ui():
    # Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)

    try:
        login(driver, "standard_user", "secret_sauce")

        wait = WebDriverWait(driver, 10)

        # Add Bike Light to cart
        bike_light = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']")))
        bike_light.click()
        time.sleep(3)

        # Add Fleece Jacket to cart
        fleece_jacket = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='add-to-cart-sauce-labs-fleece-jacket']")))
        fleece_jacket.click()
        time.sleep(3)

        # Assert cart badge displays '2'
        cart_badge = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='shopping_cart_container']/a/span")))
        assert cart_badge.text == '2'

        # Remove Bike Light from cart
        remove_bike_light = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='remove-sauce-labs-bike-light']")))
        remove_bike_light.click()
        time.sleep(3)

        # Remove Fleece Jacket from cart
        remove_fleece_jacket = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='remove-sauce-labs-fleece-jacket']")))
        remove_fleece_jacket.click()
        time.sleep(3)

        # Assert cart badge does not exist
        assert not driver.find_elements(By.XPATH, "//*[@id='shopping_cart_container']/a/span")

        # Add Bolt T-Shirt to cart
        bolt_tshirt = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']")))
        bolt_tshirt.click()
        time.sleep(3)

        # Assert cart badge displays '1'
        cart_badge = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='shopping_cart_container']/a/span")))
        assert cart_badge.text == '1'

        sys.exit(0)  # Test case passed

    except Exception as e:
        print(f"Test Failed: {e}")
        sys.exit(1)  # Test case failed

    finally:
        driver.quit()

test_ui()
