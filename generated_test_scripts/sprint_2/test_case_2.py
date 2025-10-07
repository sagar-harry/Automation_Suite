
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

class LoginPage:
    def login(self, driver, username, password):
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        ).send_keys(username)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        ).send_keys(password)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        ).click()

def run_test():
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--disable-features=NetworkService')

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    try:
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        login_page = LoginPage()
        login_page.login(driver, "standard_user", "secret_sauce")
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bike-light"))
        ).click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-fleece-jacket"))
        ).click()
        time.sleep(3)

        cart_badge = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )

        assert cart_badge.text == '2', "Cart count is incorrect"
        
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\cart_snapshot.png")
        
        sys.exit(0)
    except Exception as e:
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error_snapshot.png")
        sys.exit(1)
    finally:
        driver.quit()

run_test()
