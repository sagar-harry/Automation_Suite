
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
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]')))
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]')))
        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]')))

        username_field.send_keys(username)
        time.sleep(3)
        password_field.send_keys(password)
        time.sleep(3)
        login_button.click()
        time.sleep(3)

def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=NetworkService")
    
    driver = webdriver.Chrome(chrome_options=options)

    try:
        driver.get("https://saucedemo.com/")
        driver.maximize_window()
        time.sleep(5)
        
        login_page = LoginPage(driver)
        login_page.login('standard_user', 'secret_sauce')

        bike_light_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        time.sleep(3)
        bike_light_button.click()

        fleece_jacket_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
        time.sleep(3)
        fleece_jacket_button.click()

        cart_icon = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]/a')))
        time.sleep(3)
        cart_icon.click()

        checkout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout"]')))
        time.sleep(3)
        checkout_button.click()

        first_name_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]')))
        last_name_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="last-name"]')))
        zip_code_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="postal-code"]')))
        time.sleep(3)

        first_name_field.send_keys('Jonnathan')
        time.sleep(3)
        last_name_field.send_keys('K')
        time.sleep(3)
        zip_code_field.send_keys('10007')
        time.sleep(3)

        continue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="continue"]')))
        time.sleep(3)
        continue_button.click()
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]')))
        
        # Save a screenshot
        screenshot_path = "C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\"
        os.makedirs(screenshot_path, exist_ok=True)
        driver.save_screenshot(os.path.join(screenshot_path, 'screenshot.png'))

        sys.exit(0)

    except Exception as e:
        driver.save_screenshot(os.path.join(screenshot_path, 'screenshot_fail.png'))
        sys.exit(1)
    
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
