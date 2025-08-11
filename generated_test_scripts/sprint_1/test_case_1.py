
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        user_name_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='user-name']"))
        )
        password_field = self.driver.find_element(By.XPATH, "//input[@id='password']")
        login_button = self.driver.find_element(By.XPATH, "//input[@id='login-button']")

        user_name_field.send_keys(username)
        password_field.send_keys(password)
        time.sleep(3)
        login_button.click()

def main():
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()

        login_page = LoginPage(driver)
        login_page.login('standard_user', 'secret_sauce')

        time.sleep(3)
        # Add 'Bike Light' to the cart
        add_bike_light_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))
        )
        add_bike_light_button.click()

        time.sleep(3)
        # Add 'Fleece Jacket' to the cart
        add_fleece_jacket_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"))
        )
        add_fleece_jacket_button.click()

        time.sleep(3)
        # Verify cart badge shows '2'
        cart_badge = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']"))
        )
        assert cart_badge.text == '2'

        # Remove 'Bike Light'
        time.sleep(3)
        remove_bike_light_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='remove-sauce-labs-bike-light']"))
        )
        remove_bike_light_button.click()

        # Remove 'Fleece Jacket'
        time.sleep(3)
        remove_fleece_jacket_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='remove-sauce-labs-fleece-jacket']"))
        )
        remove_fleece_jacket_button.click()

        time.sleep(3)
        # Ensure cart badge no longer exists
        assert len(driver.find_elements(By.XPATH, "//span[@class='shopping_cart_badge']")) == 0

        # Add 'Bolt T-Shirt' to the cart
        time.sleep(3)
        add_bolt_tshirt_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"))
        )
        add_bolt_tshirt_button.click()

        # Verify cart badge shows '1'
        time.sleep(3)
        cart_badge = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']"))
        )
        assert cart_badge.text == '1'

        # Save a screenshot
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
        
        sys.exit(0)

    except Exception as e:
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error_screenshot.png")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
