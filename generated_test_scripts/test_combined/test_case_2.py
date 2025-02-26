
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
        username_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]')))
        password_field = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')

        username_field.send_keys(username)
        password_field.send_keys(password)
        time.sleep(3)  # Wait for 3 secs before clicking login button
        login_button.click()

def test_ui_scenario():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get('https://saucedemo.com/')
    time.sleep(5)  # Wait for 5 secs after opening the page

    login_page = LoginPage(driver)
    login_page.login('standard_user', 'secret_sauce')

    time.sleep(3)  # Wait for next action
    bike_light = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
    bike_light.click()

    time.sleep(3)
    fleece_jacket = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
    fleece_jacket.click()

    time.sleep(3)
    cart_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]/a')))
    cart_icon.click()

    time.sleep(3)
    checkout = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout"]')))
    checkout.click()

    time.sleep(3)
    first_name_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]')))
    last_name_field = driver.find_element(By.XPATH, '//*[@id="last-name"]')
    zip_code_field = driver.find_element(By.XPATH, '//*[@id="postal-code"]')

    first_name_field.send_keys('somename')
    last_name_field.send_keys('lastname')
    zip_code_field.send_keys('123456')

    time.sleep(3)
    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="continue"]')))
    continue_button.click()

    time.sleep(3)
    try:
        payment_info_label = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]')))
        with open("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\name_of_the_python_script.png", "wb") as file:
            file.write(driver.get_screenshot_as_png())
        sys.exit(0)
    except:
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    test_ui_scenario()
