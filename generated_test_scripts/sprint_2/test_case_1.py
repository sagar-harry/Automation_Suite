
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        user_name_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='user-name']"))
        )
        user_name_input.send_keys(username)
        time.sleep(3)
        
        password_input = self.driver.find_element(By.XPATH, "//input[@id='password']")
        password_input.send_keys(password)
        time.sleep(3)

        login_button = self.driver.find_element(By.XPATH, "//input[@id='login-button']")
        login_button.click()
        time.sleep(3)

def run_test():
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=NetworkService")

    try:
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        bike_light_add_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))
        )
        bike_light_add_btn.click()
        time.sleep(3)

        fleece_jacket_add_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"))
        )
        fleece_jacket_add_btn.click()
        time.sleep(3)

        cart_icon = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
        cart_icon.click()
        time.sleep(3)

        checkout_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='checkout']"))
        )
        checkout_btn.click()
        time.sleep(3)

        first_name_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='first-name']"))
        )
        first_name_input.send_keys("Jonnathan")
        time.sleep(3)

        last_name_input = driver.find_element(By.XPATH, "//input[@id='last-name']")
        last_name_input.send_keys("K")
        time.sleep(3)

        postal_code_input = driver.find_element(By.XPATH, "//input[@id='postal-code']")
        postal_code_input.send_keys("10007")
        time.sleep(3)

        continue_btn = driver.find_element(By.XPATH, "//input[@id='continue']")
        continue_btn.click()
        time.sleep(3)

        finish_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='finish']"))
        )
        finish_btn.click()
        time.sleep(3)

        burger_menu_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='react-burger-menu-btn']"))
        )
        burger_menu_btn.click()
        time.sleep(3)

        logout_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='logout_sidebar_link']"))
        )
        logout_btn.click()
        time.sleep(3)

        driver.save_screenshot("C:/Users/Administrator/Desktop/QE_COE/automated_pipeline_2/captured_screenshots/snapshot.png")
        sys.exit(0)

    except Exception as e:
        driver.save_screenshot("C:/Users/Administrator/Desktop/QE_COE/automated_pipeline_2/captured_screenshots/snapshot.png")
        sys.exit(1)
    finally:
        driver.quit()

run_test()
