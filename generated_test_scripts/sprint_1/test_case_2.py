
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='user-name']"))
        ).send_keys(username)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))
        ).send_keys(password)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']"))
        ).click()

def run_test():
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-features=NetworkService")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)
    driver.get("https://saucedemo.com/")
    driver.maximize_window()
    time.sleep(5)

    try:
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))
        ).click()

        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"))
        ).click()
        
        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='shopping_cart_link']"))
        ).click()
        
        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='checkout']"))
        ).click()

        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='first-name']"))
        ).send_keys("Jonnathan")

        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='last-name']"))
        ).send_keys("K")

        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='postal-code']"))
        ).send_keys("10007")

        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='continue']"))
        ).click()
        
        time.sleep(3)
        payment_info = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Payment Information')]"))
        )
        
        if payment_info.is_displayed():
            driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\payment_info.png")
            driver.quit()
            sys.exit(0)

    except Exception as e:
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\capture_screenshot\error.png")
        driver.quit()
        sys.exit(1)

run_test()
