
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='user-name']"))
        )
        password_input = self.driver.find_element(By.XPATH, "//input[@id='password']")
        login_button = self.driver.find_element(By.XPATH, "//input[@id='login-button']")
        
        username_input.send_keys(username)
        time.sleep(3)
        password_input.send_keys(password)
        time.sleep(3)
        login_button.click()

def main_test():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-features=NetworkService")

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        bike_light_add_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))
        )
        fleece_jacket_add_button = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
        
        bike_light_add_button.click()
        time.sleep(3)
        fleece_jacket_add_button.click()
        time.sleep(3)

        cart_badge = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']"))
        )

        assert cart_badge.text == '2', "Cart badge does not display '2'"

        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\test_passed.png")
        
        sys.exit(0)
 
    except Exception as e:
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\test_failed.png")
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    main_test()
