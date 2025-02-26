
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
    
    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(3)

def setUp():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popups")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=NetworkService")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    return driver

def test_payment_information_label():
    try:
        driver = setUp()
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        ).click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        ).click()
        time.sleep(3)
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a'))
        ).click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="checkout"]'))
        ).click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="first-name"]'))
        ).send_keys('somename')
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="last-name"]'))
        ).send_keys('lastname')
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="postal-code"]'))
        ).send_keys('123456')
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="continue"]'))
        ).click()
        time.sleep(3)

        payment_info_card = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]'))
        )

        if payment_info_card.is_displayed():
            print("Test Passed: Payment Information label is visible")
            sys.exit(0)
        else:
            print("Test Failed: Payment Information label is not visible")
            sys.exit(1)

    except Exception as e:
        print(f"Test Failed: {e}")
        sys.exit(1)
    finally:
        driver.quit()

test_payment_information_label()
