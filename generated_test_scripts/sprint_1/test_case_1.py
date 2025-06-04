
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()
        time.sleep(3)

def test_add_remove_cart_items():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--disable-features=NetworkService')

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    try:
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))
        ).click()
        time.sleep(3)

        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
        time.sleep(3)

        cart_badge = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']"))
        )
        assert cart_badge.text == '2', "Cart badge count is incorrect"
        time.sleep(3)

        driver.find_element(By.XPATH, "//button[@id='remove-sauce-labs-bike-light']").click()
        time.sleep(3)

        driver.find_element(By.XPATH, "//button[@id='remove-sauce-labs-fleece-jacket']").click()
        time.sleep(3)

        cart_badge = driver.find_elements(By.XPATH, "//span[@class='shopping_cart_badge']")
        assert not cart_badge, "Cart badge should not exist"
        time.sleep(3)

        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
        time.sleep(3)

        cart_badge = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']"))
        )
        assert cart_badge.text == '1', "Cart badge count is incorrect"
        time.sleep(3)

        sys.exit(0)

    except Exception as e:
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error_screenshot.png")
        sys.exit(1)

    finally:
        driver.quit()

test_add_remove_cart_items()
