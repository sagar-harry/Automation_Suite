
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.get("https://saucedemo.com/")
        time.sleep(5)
        self.driver.maximize_window()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='user-name']"))).send_keys(username)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))).send_keys(password)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']"))).click()
        time.sleep(3)

def test_cart_operations():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")
    
    driver = webdriver.Chrome(options=options)
    try:
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"))).click()
        time.sleep(3)
        
        cart_badge = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
        assert cart_badge.text == '2'
        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='remove-sauce-labs-bike-light']"))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='remove-sauce-labs-fleece-jacket']"))).click()
        time.sleep(3)

        try:
            driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
            raise AssertionError("Cart badge should not exist")
        except NoSuchElementException:
            pass
        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"))).click()
        time.sleep(3)

        cart_badge = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
        assert cart_badge.text == '1'
        sys.exit(0)
        
    except Exception as e:
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    test_cart_operations()
