
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import sys

def test_ui_scenario():
    try:
        options = Options()
        options.add_argument("--incognito")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-features=NetworkService")

        driver = webdriver.Chrome(options=options)

        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()

        class LoginPage:
            def __init__(self, driver):
                self.driver = driver
                self.username_field = self.driver.find_element(By.XPATH, "//input[@id='user-name']")
                self.password_field = self.driver.find_element(By.XPATH, "//input[@id='password']")
                self.login_button = self.driver.find_element(By.XPATH, "//input[@id='login-button']")

            def login(self, username, password):
                time.sleep(3)
                self.username_field.send_keys(username)
                time.sleep(3)
                self.password_field.send_keys(password)
                time.sleep(3)
                self.login_button.click()

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        time.sleep(3)
        bike_light_button = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
        bike_light_button.click()

        time.sleep(3)
        fleece_jacket_button = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
        fleece_jacket_button.click()

        time.sleep(3)
        cart_button = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
        cart_button.click()

        time.sleep(3)
        checkout_button = driver.find_element(By.XPATH, "//button[@id='checkout']")
        checkout_button.click()

        time.sleep(3)
        first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
        first_name.send_keys("Jonnathan")

        time.sleep(3)
        last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
        last_name.send_keys("K")

        time.sleep(3)
        zip_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
        zip_code.send_keys("10007")

        time.sleep(3)
        continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
        continue_button.click()

        time.sleep(3)
        payment_information_label = driver.find_element(By.XPATH, "//div[text()='Payment Information']")

        assert payment_information_label.is_displayed()

        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\payment_information.png")
        print("Test Passed")
        sys.exit(0)
        
    except Exception as e:
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\failure.png")
        print("Test Failed")
        print(str(e))
        sys.exit(1)
    
    finally:
        driver.quit()

test_ui_scenario()
