
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys

def wait_for_element(driver, by, value, timeout=10):
    counter = 0
    while counter < timeout:
        try:
            element = driver.find_element(by, value)
            if element:
                return element
        except Exception:
            time.sleep(1)
            counter += 1
    raise Exception(f"Element not found: {value}")

def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-features=NetworkService")

    try:
        driver = webdriver.Chrome(options=options)
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()

        my_login_page = LoginPage(driver)
        my_login_page.login("standard_user", "secret_sauce")

        time.sleep(3)
        
        wait_for_element(driver, By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)
        
        wait_for_element(driver, By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)

        cart_badge = wait_for_element(driver, By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
        
        # Check if the cart badge is '2'
        if cart_badge == '2':
            driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png')
            sys.exit(0)
        else:
            driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot_failed.png')
            sys.exit(1)

    except Exception as e:
        driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot_exception.png')
        sys.exit(1)

    finally:
        driver.quit()

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = '//*[@id="user-name"]'
        self.password_field = '//*[@id="password"]'
        self.login_button = '//*[@id="login-button"]'

    def login(self, username, password):
        username_input = wait_for_element(self.driver, By.XPATH, self.username_field)
        username_input.send_keys(username)
        time.sleep(3)

        password_input = wait_for_element(self.driver, By.XPATH, self.password_field)
        password_input.send_keys(password)
        time.sleep(3)

        login_btn = wait_for_element(self.driver, By.XPATH, self.login_button)
        login_btn.click()
        time.sleep(3)

if __name__ == "__main__":
    main()
