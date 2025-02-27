
import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

def test_cart_badge():
    try:
        chrome_options = Options()
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument('--disable-popups')
        chrome_options.add_argument('--incognito')
        chrome_options.add_argument('--disable-features=NetworkService')

        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()

        driver.get('https://saucedemo.com/')
        time.sleep(5)

        login_page = LoginPage(driver)
        login_page.login('standard_user', 'secret_sauce')

        wait = WebDriverWait(driver, 10)

        bike_light = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        bike_light.click()
        time.sleep(3)

        fleece_jacket = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
        fleece_jacket.click()
        time.sleep(3)

        cart_badge = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        assert cart_badge.text == '2'

        driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\cart_badge.png')
        driver.quit()
        sys.exit(0)

    except Exception as e:
        driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error.png')
        driver.quit()
        sys.exit(1)

test_cart_badge()
