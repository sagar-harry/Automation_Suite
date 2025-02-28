
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import sys
import os

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        )
        password_field = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')

        username_field.send_keys(username)
        sleep(3)
        password_field.send_keys(password)
        sleep(3)
        login_button.click()

def test_checkout():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-features=NetworkService")
    
    driver = webdriver.Chrome(options=options)  # Set the chromedriver path in system PATH
    driver.maximize_window()
    driver.get("https://saucedemo.com/")
    sleep(5)

    try:
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        bike_light = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        )
        fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')

        bike_light.click()
        sleep(3)
        fleece_jacket.click()
        sleep(3)

        cart_icon = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
        cart_icon.click()
        sleep(3)

        checkout = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout"]'))
        )
        checkout.click()
        sleep(3)

        first_name = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]'))
        )
        last_name = driver.find_element(By.XPATH, '//*[@id="last-name"]')
        zip_code = driver.find_element(By.XPATH, '//*[@id="postal-code"]')

        first_name.send_keys('Jonnathan')
        sleep(3)
        last_name.send_keys('K')
        sleep(3)
        zip_code.send_keys('10007')
        sleep(3)

        continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
        continue_button.click()
        sleep(3)

        payment_info = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]'))
        )

        screenshot_dir = "C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        driver.save_screenshot(os.path.join(screenshot_dir, "payment_info_visible.png"))

        assert payment_info.is_displayed()
        
        sys.exit(0)

    except Exception as e:
        driver.save_screenshot(os.path.join(screenshot_dir, "error_screenshot.png"))
        print(f"Test failed: {e}")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    test_checkout()
