
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
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(3)

def run_test():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--incognito')
    options.add_argument('--disable-features=NetworkService')

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        )

        bike_light = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        bike_light.click()
        time.sleep(3)

        fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        fleece_jacket.click()
        time.sleep(3)

        cart_count_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        )

        cart_count = cart_count_element.text
        time.sleep(3)

        if cart_count == '2':
            print("Test Passed")
            sys.exit(0)
        else:
            print("Test Failed: Cart count is not 2")
            sys.exit(1)

    except Exception as e:
        print(f"Test Failed: {str(e)}")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    run_test()
