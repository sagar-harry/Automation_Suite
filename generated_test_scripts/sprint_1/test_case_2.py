
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys

class LoginPage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        
    def login(self, username, password):
        self.driver.get(self.url)
        time.sleep(5)
        
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        )
        username_field.send_keys(username)
        time.sleep(3)
        
        password_field = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        password_field.send_keys(password)
        time.sleep(3)
        
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')
        ActionChains(self.driver).move_to_element(login_button).click(login_button).perform()
        time.sleep(3)
        

def run_test_case():
    try:
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_argument("--incognito")
        options.add_argument("--disable-features=NetworkService")
        
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        
        login_page = LoginPage(driver, 'https://saucedemo.com/')
        login_page.login('standard_user', 'secret_sauce')
        
        bike_light = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        )
        ActionChains(driver).move_to_element(bike_light).click(bike_light).perform()
        time.sleep(3)

        fleece_jacket = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        )
        ActionChains(driver).move_to_element(fleece_jacket).click(fleece_jacket).perform()
        time.sleep(3)

        cart_icon = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
        ActionChains(driver).move_to_element(cart_icon).click(cart_icon).perform()
        time.sleep(3)
        
        checkout_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="checkout"]'))
        )
        ActionChains(driver).move_to_element(checkout_button).click(checkout_button).perform()
        time.sleep(3)

        first_name_field = driver.find_element(By.XPATH, '//*[@id="first-name"]')
        first_name_field.send_keys('Jonnathan')
        time.sleep(3)

        last_name_field = driver.find_element(By.XPATH, '//*[@id="last-name"]')
        last_name_field.send_keys('K')
        time.sleep(3)

        zip_code_field = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
        zip_code_field.send_keys('10007')
        time.sleep(3)

        continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
        ActionChains(driver).move_to_element(continue_button).click(continue_button).perform()
        time.sleep(3)

        payment_information_label = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]'))
        )

        if payment_information_label.is_displayed():
            driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\payment_information.png")
            driver.quit()
            sys.exit(0)
    except Exception as e:
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error.png")
        driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    run_test_case()
