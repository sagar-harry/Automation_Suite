
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = '//*[@id="user-name"]'
        self.password_field = '//*[@id="password"]'
        self.login_button = '//*[@id="login-button"]'

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.username_field)))
        self.driver.find_element(By.XPATH, self.username_field).send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.password_field).send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.login_button).click()

def test_add_items_to_cart():
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://saucedemo.com/")
        driver.maximize_window()
        time.sleep(5)

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        bike_light = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        bike_light.click()
        time.sleep(3)

        fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        fleece_jacket.click()
        time.sleep(3)

        cart_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        assert cart_count.text == '2', f"Expected cart count to be '2', but got '{cart_count.text}'"

        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")

        sys.exit(0)

    except Exception as e:
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error_screenshot.png")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    test_add_items_to_cart()
