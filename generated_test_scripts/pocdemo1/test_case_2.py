
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
        self.driver.get("https://saucedemo.com/")
        time.sleep(5)
        self.driver.maximize_window()

        wait = WebDriverWait(self.driver, 10)
        username_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]')))
        password_input = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')

        username_input.send_keys(username)
        time.sleep(3)
        password_input.send_keys(password)
        time.sleep(3)
        login_button.click()
        time.sleep(3)

def run_test():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)
    try:
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        
        wait = WebDriverWait(driver, 10)
        bike_light_btn = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        fleece_jacket_btn = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')

        bike_light_btn.click()
        time.sleep(3)
        fleece_jacket_btn.click()
        time.sleep(3)

        cart_count = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        if cart_count.text == '2':
            sys.exit(0)
        else:
            sys.exit(1)

    except Exception as e:
        print("Test failed:", e)
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    run_test()
