
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        user_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'user-name'))
        )
        user_field.send_keys(username)
        time.sleep(3)
        
        pass_field = self.driver.find_element(By.ID, 'password')
        pass_field.send_keys(password)
        time.sleep(3)
        
        login_button = self.driver.find_element(By.ID, 'login-button')
        login_button.click()
        time.sleep(3)

def run_test():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        bike_light_add_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'add-to-cart-sauce-labs-bike-light'))
        )
        bike_light_add_button.click()
        time.sleep(3)

        fleece_jacket_add_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'add-to-cart-sauce-labs-fleece-jacket'))
        )
        fleece_jacket_add_button.click()
        time.sleep(3)

        cart_badge = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'shopping_cart_badge'))
        )
        cart_count_text = cart_badge.text
        assert cart_count_text == '2', f"Expected cart count to be '2', but got: {cart_count_text}"

        print("Test case passed.")
        sys.exit(0)
        
    except Exception as e:
        print("Test case failed:", str(e))
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")
        sys.exit(1)
        
    finally:
        driver.quit()

if __name__ == '__main__':
    run_test()
