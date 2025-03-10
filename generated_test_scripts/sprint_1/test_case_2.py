
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = '//*[@id="user-name"]'
        self.password_input = '//*[@id="password"]'
        self.login_button = '//*[@id="login-button"]'

    def login(self, username, password):
        self.driver.find_element(By.XPATH, self.username_input).send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.password_input).send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.login_button).click() 
        time.sleep(3)

def test_scenario():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)
    try:
        driver.maximize_window()
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        bike_light = '//*[@id="add-to-cart-sauce-labs-bike-light"]'
        fleece_jacket = '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'
        cart_icon = '//*[@id="shopping_cart_container"]/a'
        checkout_button = '//*[@id="checkout"]'
        first_name_field = '//*[@id="first-name"]'
        last_name_field = '//*[@id="last-name"]'
        zip_code_field = '//*[@id="postal-code"]'
        continue_button = '//*[@id="continue"]'
        payment_info_label = '//*[@id="checkout_summary_container"]/div/div[2]/div[1]'

        driver.find_element(By.XPATH, bike_light).click()
        time.sleep(3)
        driver.find_element(By.XPATH, fleece_jacket).click()
        time.sleep(3)
        driver.find_element(By.XPATH, cart_icon).click()
        time.sleep(3)
        driver.find_element(By.XPATH, checkout_button).click()
        time.sleep(3)
        driver.find_element(By.XPATH, first_name_field).send_keys('Jonnathan')
        time.sleep(3)
        driver.find_element(By.XPATH, last_name_field).send_keys('K')
        time.sleep(3)
        driver.find_element(By.XPATH, zip_code_field).send_keys('10007')
        time.sleep(3)
        driver.find_element(By.XPATH, continue_button).click()
        time.sleep(3)

        payment_info_visible = driver.find_element(By.XPATH, payment_info_label).is_displayed()
        
        if payment_info_visible:
            print("Test Passed: Payment Information is visible.")
            sys.exit(0)
        else:
            print("Test Failed: Payment Information is not visible.")
            sys.exit(1)

    except Exception as e:
        print(f"Test Failed: {e}")
        sys.exit(1)

    finally:
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
        driver.quit()

test_scenario()
