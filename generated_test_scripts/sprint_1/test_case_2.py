
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
    def login(self, username, password):
        username_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]')))
        password_input = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')
        
        time.sleep(3)
        username_input.send_keys(username)
        time.sleep(3)
        password_input.send_keys(password)
        time.sleep(3)
        login_button.click()

def run_test():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")

    try:
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        
        bike_light_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        fleece_jacket_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        
        time.sleep(3)
        bike_light_button.click()
        time.sleep(3)
        fleece_jacket_button.click()
        
        cart_icon = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
        time.sleep(3)
        cart_icon.click()
        
        checkout_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="checkout"]')))
        time.sleep(3)
        checkout_button.click()
        
        first_name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="first-name"]')))
        last_name_input = driver.find_element(By.XPATH, '//*[@id="last-name"]')
        zip_code_input = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
        
        time.sleep(3)
        first_name_input.send_keys("Jonnathan")
        time.sleep(3)
        last_name_input.send_keys("K")
        time.sleep(3)
        zip_code_input.send_keys("10007")
        
        continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
        time.sleep(3)
        continue_button.click()
        
        payment_info_label = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]')))
        
        if payment_info_label.is_displayed():
            print("Test Passed")
            driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\test_passed.png')
            sys.exit(0)
        else:
            print("Payment information label not displayed.")
            driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\test_failed.png')
            sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\test_failed.png')
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    run_test()
