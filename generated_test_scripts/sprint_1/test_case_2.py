
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import sys

class LoginPage:
    def login(self, driver, username, password):
        username_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        )
        password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
        
        username_field.send_keys(username)
        password_field.send_keys(password)
        time.sleep(3)
        login_button.click()
        time.sleep(3)

def test_ui_scenario():
    url = "https://saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"
    
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-features=NetworkService")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(5)
    driver.maximize_window()
    time.sleep(3)

    login_page = LoginPage()
    login_page.login(driver, username, password)
    
    bike_light_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
    )
    fleece_jacket_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
    
    bike_light_button.click()
    time.sleep(3)
    fleece_jacket_button.click()
    time.sleep(3)
    
    cart_icon = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a'))
    )
    cart_icon.click()
    time.sleep(3)
    
    checkout_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout"]'))
    )
    checkout_button.click()
    time.sleep(3)
    
    first_name_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]'))
    )
    last_name_field = driver.find_element(By.XPATH, '//*[@id="last-name"]')
    zip_code_field = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
    
    first_name_field.send_keys('somename')
    last_name_field.send_keys('lastname')
    zip_code_field.send_keys('123456')
    time.sleep(3)
    
    continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
    continue_button.click()
    time.sleep(3)
    
    try:
        payment_info_label = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]'))
        )
        if payment_info_label.is_displayed():
            print("Test passed")
            sys.exit(0)
    except:
        print("Test failed")
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    test_ui_scenario()
