
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
        self.driver.get('https://saucedemo.com/')
        self.driver.maximize_window()
        time.sleep(5)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys(username)
        
        time.sleep(3)
        
        self.driver.find_element(By.ID, "password").send_keys(password)
        
        time.sleep(3)
        
        self.driver.find_element(By.ID, "login-button").click()
        
        time.sleep(3)

class UITests:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-notifications')
        options.add_argument('--incognito')
        options.add_argument('--disable-features=NetworkService')
        
        self.driver = webdriver.Chrome(options=options)

    def run_test_case(self):
        try:
            login_page = LoginPage(self.driver)
            login_page.login('standard_user', 'secret_sauce')
            
            add_bike_light = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "add-to-cart-sauce-labs-bike-light"))
            )
            add_bike_light.click()
            
            time.sleep(3)
            
            add_fleece_jacket = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
            add_fleece_jacket.click()
            
            time.sleep(3)
            
            cart_badge = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
            )
            assert cart_badge.text == '2', 'Cart badge does not display 2'

            time.sleep(3)
            
            remove_bike_light = self.driver.find_element(By.ID, "remove-sauce-labs-bike-light")
            remove_bike_light.click()
            
            time.sleep(3)
            
            remove_fleece_jacket = self.driver.find_element(By.ID, "remove-sauce-labs-fleece-jacket")
            remove_fleece_jacket.click()

            time.sleep(3)

            cart_badge_disappear = WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element((By.CLASS_NAME, "shopping_cart_badge"))
            )
            assert not cart_badge_disappear, 'Cart count element should not exist'

            time.sleep(3)
            
            add_bolt_tshirt = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
            add_bolt_tshirt.click()

            time.sleep(3)
            
            cart_badge = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
            )
            assert cart_badge.text == '1', 'Cart badge does not display 1'

            time.sleep(3)
            
            self.driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\final_state.png")

            sys.exit(0)
        except Exception as e:
            self.driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error_state.png")
            sys.exit(1)
        finally:
            self.driver.quit()

if __name__ == "__main__":
    test = UITests()
    test.run_test_case()
