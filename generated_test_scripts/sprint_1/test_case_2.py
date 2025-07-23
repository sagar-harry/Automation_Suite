
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        wait = WebDriverWait(self.driver, 30)
        username_input = wait.until(EC.visibility_of_element_located((By.ID, 'user-name')))
        password_input = wait.until(EC.visibility_of_element_located((By.ID, 'password')))
        login_button = wait.until(EC.element_to_be_clickable((By.ID, 'login-button')))

        username_input.send_keys(username)
        password_input.send_keys(password)
        time.sleep(3)
        login_button.click()

def run_test():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-features=NetworkService")
        
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://saucedemo.com/')
        time.sleep(5)
        driver.maximize_window()

        login_page = LoginPage(driver)
        login_page.login('standard_user', 'secret_sauce')

        wait = WebDriverWait(driver, 30)
        time.sleep(3)
        bike_light_add_button = wait.until(EC.element_to_be_clickable((By.ID, 'add-to-cart-sauce-labs-bike-light')))
        bike_light_add_button.click()
        
        time.sleep(3)
        fleece_jacket_add_button = wait.until(EC.element_to_be_clickable((By.ID, 'add-to-cart-sauce-labs-fleece-jacket')))
        fleece_jacket_add_button.click()

        time.sleep(3)
        cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'shopping_cart_link')))
        cart_button.click()

        time.sleep(3)
        checkout_button = wait.until(EC.element_to_be_clickable((By.ID, 'checkout')))
        checkout_button.click()

        time.sleep(3)
        first_name_input = wait.until(EC.visibility_of_element_located((By.ID, 'first-name')))
        last_name_input = wait.until(EC.visibility_of_element_located((By.ID, 'last-name')))
        postal_code_input = wait.until(EC.visibility_of_element_located((By.ID, 'postal-code')))
        continue_button = wait.until(EC.element_to_be_clickable((By.ID, 'continue')))

        first_name_input.send_keys('Jonnathan')
        last_name_input.send_keys('K')
        postal_code_input.send_keys('10007')
        time.sleep(3)
        
        continue_button.click()
        
        payment_info_label = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Payment Information')]")))
        
        # Taking snapshot of the page
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\final_step.png")

        print("Test Passed")
        sys.exit(0)

    except Exception as e:
        print(f"Test Failed: {e}")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    run_test()
