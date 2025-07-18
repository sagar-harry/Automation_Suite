
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='user-name']"))).send_keys(username)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()

def test_shopping_cart():
    # Setup ChromeOptions
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--headless")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-features=NetworkService")
    
    # Setup WebDriver
    driver = webdriver.Chrome(options=options)
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    driver.maximize_window()

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    
    time.sleep(3)
    try:
        # Add Bike Light to cart
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))).click()
        time.sleep(3)
        
        # Add Fleece Jacket to cart
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"))).click()
        time.sleep(3)
        
        # Check cart badge for '2'
        cart_badge = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']")))
        assert cart_badge.text == '2', "Cart badge displays incorrect count"
        time.sleep(3)
        
        # Remove Bike Light
        driver.find_element(By.XPATH, "//button[@id='remove-sauce-labs-bike-light']").click()
        time.sleep(3)
        
        # Remove Fleece Jacket
        driver.find_element(By.XPATH, "//button[@id='remove-sauce-labs-fleece-jacket']").click()
        time.sleep(3)
        
        # Verify cart badge does not exist
        assert len(driver.find_elements(By.XPATH, "//span[@class='shopping_cart_badge']")) == 0, "Cart badge still exists"
        
        # Add Bolt T-Shirt
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"))).click()
        time.sleep(3)
        
        # Verify cart badge for '1'
        cart_badge = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']")))
        assert cart_badge.text == '1', "Cart badge displays incorrect count"

        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
        driver.quit()
        sys.exit(0)
        
    except Exception as e:
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot_error.png")
        driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    test_shopping_cart()
