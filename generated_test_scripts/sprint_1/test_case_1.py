
import time
import sys
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_element = self.driver.find_element(By.XPATH, '//*[@id="user-name"]')
        password_element = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')
        
        username_element.send_keys(username)
        password_element.send_keys(password)
        time.sleep(3)
        login_button.click()

def test_cart_operations():
    try:
        # Browser Options
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-features=NetworkService")

        # Initialize WebDriver
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()

        # Open URL
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        # Login
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        
        # Wait for elements to load and perform actions
        bike_light = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        )
        fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')

        bike_light.click()
        time.sleep(3)
        fleece_jacket.click()

        cart_count = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        )
        assert cart_count.text == '2'

        remove_bike_light = driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]')
        remove_fleece_jacket = driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]')

        remove_bike_light.click()
        time.sleep(3)
        remove_fleece_jacket.click()

        assert not driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')

        bolt_tshirt = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        bolt_tshirt.click()
        time.sleep(3)

        cart_count = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        )
        assert cart_count.text == '1'

        # Save the snapshot
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")

        sys.exit(0)

    except Exception as e:
        # Save the snapshot
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error_screenshot.png")
        print(traceback.format_exc())
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    test_cart_operations()
