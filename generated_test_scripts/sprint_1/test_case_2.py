
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import sys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys(username)
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//*[@id='login-button']").click()

def run_test():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        time.sleep(3)

        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']"))).click()
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']"))).click()
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='shopping_cart_container']/a"))).click()
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='checkout']"))).click()
        time.sleep(3)

        wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='first-name']"))).send_keys("somename")
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='last-name']").send_keys("lastname")
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='postal-code']").send_keys("123456")
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='continue']"))).click()
        time.sleep(3)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[1]")))
        print("Test case passed.")
        sys.exit(0)
    except (TimeoutException, NoSuchElementException):
        print("Test case failed.")
        sys.exit(1)
    finally:
        driver.quit()

run_test()
