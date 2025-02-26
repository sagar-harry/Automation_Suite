
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        user_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        )
        user_input.clear()
        user_input.send_keys(username)
        time.sleep(3)
        
        password_input = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        password_input.clear()
        password_input.send_keys(password)
        time.sleep(3)

        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')
        login_button.click()
        time.sleep(3)

def test_payment_information_visibility():
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    driver.maximize_window()

    try:
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        bike_light = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        )
        bike_light.click()
        time.sleep(3)

        fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        fleece_jacket.click()
        time.sleep(3)

        cart_icon = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
        cart_icon.click()
        time.sleep(3)

        checkout_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="checkout"]'))
        )
        checkout_button.click()
        time.sleep(3)

        first_name = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="first-name"]'))
        )
        first_name.clear()
        first_name.send_keys("somename")
        time.sleep(3)

        last_name = driver.find_element(By.XPATH, '//*[@id="last-name"]')
        last_name.clear()
        last_name.send_keys("lastname")
        time.sleep(3)

        zip_code = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
        zip_code.clear()
        zip_code.send_keys("123456")
        time.sleep(3)

        continue_btn = driver.find_element(By.XPATH, '//*[@id="continue"]')
        continue_btn.click()
        time.sleep(3)

        payment_info_label = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]'))
        )

        if payment_info_label.is_displayed():
            print("Test Passed: Payment information label is visible")
            sys.exit(0)
        else:
            print("Test Failed: Payment information label is not visible")
            sys.exit(1)

    except Exception as e:
        print(f"Test Failed: {str(e)}")
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    test_payment_information_visibility()
