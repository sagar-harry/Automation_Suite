
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import sys
import os

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        user_elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]')))
        password_elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
        login_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login-button"]')))
        
        user_elem.send_keys(username)
        time.sleep(3)
        password_elem.send_keys(password)
        time.sleep(3)
        login_button.click()
        time.sleep(3)

def test_cart_count():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)
    try:
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        bike_light = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        fleece_jacket = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
        
        time.sleep(3)
        bike_light.click()
        time.sleep(3)
        fleece_jacket.click()
        time.sleep(3)

        cart_count = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))

        if cart_count.text == "2":
            screenshot_path = os.path.join("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots", "test_passed.png")
            driver.save_screenshot(screenshot_path)
            sys.exit(0)
        else:
            screenshot_path = os.path.join("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots", "test_failed.png")
            driver.save_screenshot(screenshot_path)
            sys.exit(1)
    except (TimeoutException, NoSuchElementException, Exception) as e:
        screenshot_path = os.path.join("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots", "exception.png")
        driver.save_screenshot(screenshot_path)
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    test_cart_count()
