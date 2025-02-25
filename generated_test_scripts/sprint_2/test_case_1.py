
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import sys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = driver.find_element(By.XPATH, '//*[@id="user-name"]')
        self.password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
        self.login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')

    def login(self, username, password):
        self.username_field.send_keys(username)
        self.password_field.send_keys(password)
        self.login_button.click()

def setup_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-notifications')
    options.add_argument('--incognito')
    options.add_argument('--disable-features=NetworkService')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver

try:
    driver = setup_driver()
    driver.get("https://saucedemo.com/")
    time.sleep(5)

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    time.sleep(3)

    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('somename')
    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('lastname')
    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys('123456')
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="finish"]').click()
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
    driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()
    time.sleep(3)

    print("Test Passed")
    sys.exit(0)

except Exception as e:
    print("Test Failed", e)
    sys.exit(1)

finally:
    driver.quit()
