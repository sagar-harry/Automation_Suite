
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import sys
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'user-name'))
        ).send_keys(username)
        time.sleep(3)
        
        self.driver.find_element(By.ID, 'password').send_keys(password)
        time.sleep(3)
        
        self.driver.find_element(By.ID, 'login-button').click()

def execute_test():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popups")
    options.add_argument("--disable-features=NetworkService")

    try:
        driver = webdriver.Chrome(options=options)
        driver.get("https://saucedemo.com/")
        driver.maximize_window()
        time.sleep(5)

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        # Add 'Bike Light' to cart
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'add-to-cart-sauce-labs-bike-light'))
        ).click()
        time.sleep(3)

        # Add 'Fleece Jacket' to cart
        driver.find_element(By.ID, 'add-to-cart-sauce-labs-fleece-jacket').click()
        time.sleep(3)

        # Proceed to checkout
        driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'checkout'))
        ).click()
        time.sleep(3)

        # Enter checkout information
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'first-name'))
        ).send_keys('Jonnathan')
        time.sleep(3)
        
        driver.find_element(By.ID, 'last-name').send_keys('K')
        time.sleep(3)
        
        driver.find_element(By.ID, 'postal-code').send_keys('10007')
        time.sleep(3)

        # Continue to next step
        driver.find_element(By.ID, 'continue').click()
        time.sleep(3)

        # Verify 'Payment Information' label is visible
        payment_info_label = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Payment Information')]"))
        )

        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\test_result.png")
        driver.quit()

        if payment_info_label:
            sys.exit(0)
        else:
            sys.exit(1)

    except Exception as e:
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error.png")
        driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    execute_test()
