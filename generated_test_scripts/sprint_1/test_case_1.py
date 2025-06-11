
import time
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='user-name']"))
        )
        password_input = self.driver.find_element(By.XPATH, "//input[@id='password']")
        login_button = self.driver.find_element(By.XPATH, "//input[@id='login-button']")
        
        time.sleep(3)  # Wait 3 seconds before action
        username_input.send_keys(username)
        password_input.send_keys(password)
        
        time.sleep(3)  # Wait 3 seconds
        login_button.click()

def main():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=NetworkService")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get("https://www.saucedemo.com/")
        time.sleep(5)  # Wait for 5 seconds after page load
        driver.maximize_window()
        
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        # Add 'Bike Light' to the cart
        add_bike_light = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))
        )
        time.sleep(3)
        add_bike_light.click()

        # Add 'Fleece Jacket' to the cart
        add_fleece_jacket = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"))
        )
        time.sleep(3)
        add_fleece_jacket.click()

        # Verify cart badge is '2'
        cart_badge = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']"))
        )
        assert cart_badge.text == '2'

        # Remove 'Bike Light'
        remove_bike_light = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='remove-sauce-labs-bike-light']"))
        )
        time.sleep(3)
        remove_bike_light.click()

        # Remove 'Fleece Jacket'
        remove_fleece_jacket = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='remove-sauce-labs-fleece-jacket']"))
        )
        time.sleep(3)
        remove_fleece_jacket.click()

        # Verify cart badge does not exist
        cart_badge_exists = True
        try:
            WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']"))
            )
        except:
            cart_badge_exists = False
        assert not cart_badge_exists

        # Add 'Bolt T-Shirt' to the cart
        add_bolt_tshirt = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"))
        )
        time.sleep(3)
        add_bolt_tshirt.click()

        # Verify cart badge is '1'
        cart_badge = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']"))
        )
        assert cart_badge.text == '1'

        sys.exit(0)

    except Exception as e:
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\failure.png")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
