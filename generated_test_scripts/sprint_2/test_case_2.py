
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
        self.username_locator = "//*[@id='user-name']"
        self.password_locator = "//*[@id='password']"
        self.login_button_locator = "//*[@id='login-button']"
    
    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.username_locator))
        ).send_keys(username)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.password_locator))
        ).send_keys(password)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.login_button_locator))
        ).click()

def main():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")
    
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        
        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']"))
        ).click()

        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']"))
        ).click()

        time.sleep(3)
        cart_count = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='shopping_cart_container']/a/span"))
        ).text

        if cart_count == '2':
            sys.exit(0)
        else:
            sys.exit(1)
            
    except Exception as e:
        print(f"Test failed due to {str(e)}")
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
