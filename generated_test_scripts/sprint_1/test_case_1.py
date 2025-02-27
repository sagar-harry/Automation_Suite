
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
    def login(self, username, password):
        username_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]')))
        password_input = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')
        
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()

def main():
    try:
        options = Options()
        options.add_argument("--incognito")
        options.add_argument("--disable-notifications")
        options.add_argument("disable-features=NetworkService")
        
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get('https://saucedemo.com/')
        
        time.sleep(5)
        
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        
        time.sleep(3)
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        ).click()
        time.sleep(3)
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]'))
        ).click()
        time.sleep(3)
        
        cart_count = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        )
        assert cart_count.text == '2'
        
        driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]').click()
        time.sleep(3)
        
        driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]').click()
        time.sleep(3)
        
        cart_count_present = False
        try:
            WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
            )
            cart_count_present = True
        except:
            cart_count_present = False
            
        assert not cart_count_present
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        ).click()
        time.sleep(3)
        
        cart_count = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        )
        assert cart_count.text == '1'
        
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\test_result.png")
        driver.quit()
        sys.exit(0)
    
    except Exception as e:
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error.png")
        driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    main()
