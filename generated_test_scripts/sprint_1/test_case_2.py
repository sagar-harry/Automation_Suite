
import time
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = "standard_user"
        self.password = "secret_sauce"
        self.username_locator = '//*[@id="user-name"]'
        self.password_locator = '//*[@id="password"]'
        self.login_button_locator = '//*[@id="login-button"]'

    def login(self):
        self.driver.find_element(By.XPATH, self.username_locator).send_keys(self.username)
        self.driver.find_element(By.XPATH, self.password_locator).send_keys(self.password)
        self.driver.find_element(By.XPATH, self.login_button_locator).click()

def take_screenshot(driver, script_name):
    driver.save_screenshot(f"C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\{script_name}_screenshot.png")

def test_purchase_flow():
    chrome_options = Options()
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--disable-popup-blocking')
    chrome_options.add_argument('--disable-features=NetworkService')

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get('https://saucedemo.com/')
    time.sleep(5)  # Wait for 5 secs after opening the page

    login_page = LoginPage(driver)
    login_page.login()

    time.sleep(3)  # Wait for 3 secs before every action
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()

    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()

    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()

    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()

    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('somename')

    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('lastname')

    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys('123456')

    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()

    time.sleep(3)
    
    # Assert that the 'Payment Information' label is visible
    try:
        payment_info_label = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]')
        assert payment_info_label.is_displayed()
        take_screenshot(driver, script_name="test_purchase_flow")
        sys.exit(0)  # Exit with success code
    except Exception as e:
        take_screenshot(driver, script_name="test_purchase_flow")
        sys.exit(1)  # Exit with failure code
    finally:
        driver.quit()

test_purchase_flow()
