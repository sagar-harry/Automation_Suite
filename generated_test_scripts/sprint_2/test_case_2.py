
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        self.driver.get("https://saucedemo.com/")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
        self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()
        time.sleep(3)

try:
    # Initialize WebDriver with options
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")
    
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    login_page = LoginPage(driver)
    login_page.login()

    # Add 'Bike Light' to the cart
    bike_light_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))
    )
    bike_light_button.click()
    time.sleep(3)

    # Add 'Fleece Jacket' to the cart
    fleece_jacket_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"))
    )
    fleece_jacket_button.click()
    time.sleep(3)

    # Verify cart count
    cart_badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']"))
    )
    
    if cart_badge.text == '2':
        screenshot_path = r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\cart_page.png"
        driver.save_screenshot(screenshot_path)
        sys.exit(0)
    else:
        sys.exit(1)

except Exception as e:
    sys.exit(1)

finally:
    driver.quit()
