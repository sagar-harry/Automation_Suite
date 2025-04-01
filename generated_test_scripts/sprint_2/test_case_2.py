
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        ).send_keys(username)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))
        ).send_keys(password)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]'))
        ).click()


def setup_browser():
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=chrome_options)
    return driver


def main():
    driver = setup_browser()
    driver.get("https://saucedemo.com/")
    time.sleep(5)  # Allow time for page to load
    driver.maximize_window()

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    time.sleep(3)

    try:
        bike_light_locator = '//*[@id="add-to-cart-sauce-labs-bike-light"]'
        fleece_jacket_locator = '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'
        cart_count_locator = '//*[@id="shopping_cart_container"]/a/span'

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, bike_light_locator))
        ).click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, fleece_jacket_locator))
        ).click()
        time.sleep(3)

        cart_count_text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, cart_count_locator))
        ).text

        assert cart_count_text == '2', "Cart count is incorrect"
        print("Test Passed: Cart count is correct")
        snapshot_path = r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots'
        driver.save_screenshot(snapshot_path + r"\cart_snapshot.png")
        sys.exit(0)

    except Exception as e:
        print(f"Test Failed: {str(e)}")
        snapshot_path = r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots'
        driver.save_screenshot(snapshot_path + r"\cart_snapshot_fail.png")
        sys.exit(1)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
