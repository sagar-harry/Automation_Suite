
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        )
        password_input = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')

        username_input.send_keys(username)
        password_input.send_keys(password)
        time.sleep(3)
        login_button.click()

def main():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-features=NetworkService")

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        # Add Bike Light
        bike_light = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        )
        time.sleep(3)
        bike_light.click()

        # Add Fleece Jacket
        fleece_jacket = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]'))
        )
        time.sleep(3)
        fleece_jacket.click()

        # Validate Cart Count
        cart_count = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        )
        assert cart_count.text == '2'

        # Remove Bike Light
        remove_bike_light = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]'))
        )
        time.sleep(3)
        remove_bike_light.click()

        # Remove Fleece Jacket
        remove_fleece_jacket = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]'))
        )
        time.sleep(3)
        remove_fleece_jacket.click()

        # Validate Cart Count Element
        cart_count = driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert len(cart_count) == 0

        # Add Bolt T-Shirt
        bolt_t_shirt = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        )
        time.sleep(3)
        bolt_t_shirt.click()

        # Validate Cart Count
        cart_count = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        )
        assert cart_count.text == '1'

        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
        sys.exit(0)

    except Exception as e:
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error_screenshot.png")
        sys.exit(1)
    
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
