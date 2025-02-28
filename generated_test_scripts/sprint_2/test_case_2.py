
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import os

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = '//*[@id="user-name"]'
        self.password_input = '//*[@id="password"]'
        self.login_button = '//*[@id="login-button"]'

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.username_input))).send_keys(username)
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.password_input))).send_keys(password)
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.login_button))).click()
        time.sleep(3)

def main():
    options = Options()
    options.add_argument('--disable-notifications')
    options.add_argument('--incognito')
    options.add_argument('--disable-features=NetworkService')

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    
    try:
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
        time.sleep(3)

        cart_count_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        time.sleep(3)

        if cart_count_element.text.strip() == '2':
            print("Test case passed")
            sys.exit(0)
        else:
            print("Test case failed")
            sys.exit(1)

    except Exception as e:
        print(f"Exception occurred: {e}")
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error_screenshot.png")
        sys.exit(1)
        
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
