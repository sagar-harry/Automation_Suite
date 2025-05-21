
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys
import traceback

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_field = self.driver.find_element(By.XPATH, '//*[@id="user-name"]')
        password_field = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')

        time.sleep(3)  # Wait before performing actions
        username_field.send_keys(username)
        time.sleep(3)
        password_field.send_keys(password)
        time.sleep(3)
        login_button.click()

def test_ui_cart_count():
    url = "https://saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"
    
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        driver.get(url)
        time.sleep(5)  # Wait for page to load
        driver.maximize_window()

        login_page = LoginPage(driver)
        login_page.login(username, password)

        bike_light = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')

        time.sleep(3)
        bike_light.click()
        time.sleep(3)
        fleece_jacket.click()
        
        cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        
        time.sleep(3)
        assert cart_count.text == '2', "Cart count did not match expected value of 2"

        snapshot_path = r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\cart_count_test.png"
        driver.save_screenshot(snapshot_path)

        sys.exit(0)
    
    except Exception as e:
        print("Test case failed.")
        print(traceback.format_exc())
        sys.exit(1)
    
    finally:
        driver.quit()

if __name__ == "__main__":
    test_ui_cart_count()
