
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import sys

try:
    options = webdriver.ChromeOptions()
    options.add_argument('disable-features=NetworkService')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--incognito')

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)

    driver.get('https://saucedemo.com/')
    driver.maximize_window()
    time.sleep(5)

    class LoginPage:
        def __init__(self, driver):
            self.driver = driver
            self.username_input = '//*[@id="user-name"]'
            self.password_input = '//*[@id="password"]'
            self.login_button = '//*[@id="login-button"]'

        def login(self, username, password):
            wait.until(EC.visibility_of_element_located((By.XPATH, self.username_input))).send_keys(username)
            time.sleep(3)
            wait.until(EC.visibility_of_element_located((By.XPATH, self.password_input))).send_keys(password)
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.XPATH, self.login_button))).click()
            time.sleep(3)

    login_page = LoginPage(driver)
    login_page.login('standard_user', 'secret_sauce')

    # Add bike light
    bike_light = '//*[@id="add-to-cart-sauce-labs-bike-light"]'
    fleece_jacket = '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]'
    cart_count = '//*[@id="shopping_cart_container"]/a/span'
    remove_bike_light = '//*[@id="remove-sauce-labs-bike-light"]'
    remove_fleece_jacket = '//*[@id="remove-sauce-labs-fleece-jacket"]'
    add_bolt_tshirt = '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'

    wait.until(EC.element_to_be_clickable((By.XPATH, bike_light))).click()
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.XPATH, fleece_jacket))).click()
    time.sleep(3)

    cart_badge = wait.until(EC.visibility_of_element_located((By.XPATH, cart_count)))
    assert cart_badge.text == '2', "Cart badge does not display '2' after adding two items"
    time.sleep(3)

    # Remove items
    wait.until(EC.element_to_be_clickable((By.XPATH, remove_bike_light))).click()
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.XPATH, remove_fleece_jacket))).click()
    time.sleep(3)

    # Verify cart badge element doesn't exist
    assert not driver.find_elements(By.XPATH, cart_count), "Cart count element still exists after removing items"
    time.sleep(3)

    # Add Bolt T-Shirt
    wait.until(EC.element_to_be_clickable((By.XPATH, add_bolt_tshirt))).click()
    time.sleep(3)

    cart_badge = wait.until(EC.visibility_of_element_located((By.XPATH, cart_count)))
    assert cart_badge.text == '1', "Cart badge does not display '1' after adding Bolt T-Shirt"
    
    # Screenshot
    screenshot_path = r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png'
    os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
    driver.save_screenshot(screenshot_path)

    driver.quit()
    sys.exit(0)

except Exception as e:
    driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error_screenshot.png')
    driver.quit()
    sys.exit(1)
