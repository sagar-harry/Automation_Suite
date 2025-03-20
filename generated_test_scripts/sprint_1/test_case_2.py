
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
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
        
        time.sleep(3)
        username_field.send_keys(username)
        time.sleep(3)
        password_field.send_keys(password)
        time.sleep(3)
        login_button.click()

def test_purchase_bike_light_and_fleece_jacket():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-notifications')
        options.add_argument('--incognito')
        options.add_argument('--disable-features=NetworkService')

        driver = webdriver.Chrome(options=options)
        driver.get('https://saucedemo.com/')
        time.sleep(5)
        driver.maximize_window()

        login_page = LoginPage(driver)
        login_page.login('standard_user', 'secret_sauce')
        
        bike_light = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        )
        time.sleep(3)
        bike_light.click()

        fleece_jacket = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        )
        time.sleep(3)
        fleece_jacket.click()

        cart_icon = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a'))
        )
        time.sleep(3)
        cart_icon.click()

        checkout = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout"]'))
        )
        time.sleep(3)
        checkout.click()

        first_name = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]'))
        )
        time.sleep(3)
        first_name.send_keys('Jonnathan')

        last_name = driver.find_element(By.XPATH, '//*[@id="last-name"]')
        time.sleep(3)
        last_name.send_keys('K')

        zip_code = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
        time.sleep(3)
        zip_code.send_keys('10007')

        continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
        time.sleep(3)
        continue_button.click()

        payment_info_card = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]'))
        )

        if payment_info_card.is_displayed():
            os.makedirs(os.path.dirname("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\"), exist_ok=True)
            driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")
            driver.quit()
            sys.exit(0)
        else:
            raise Exception("Payment Information not visible")

    except Exception as e:
        driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    test_purchase_bike_light_and_fleece_jacket()
