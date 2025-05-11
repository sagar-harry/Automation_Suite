
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_field = self.driver.find_element(By.XPATH, '//*[@id="user-name"]')
        password_field = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')
        
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

def test_ui_scenario():
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_experimental_option("prefs", { \
        "profile.default_content_setting_values.notifications": 2
    })
    options.add_argument('--disable-features=NetworkService')
    
    try:
        driver = webdriver.Chrome(options=options)
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()
        
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        time.sleep(3)
        
        bike_light = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        bike_light.click()
        time.sleep(3)
        
        fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')
        fleece_jacket.click()
        time.sleep(3)
        
        cart_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert cart_badge.text == '2'
        
        remove_bike_light = driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]')
        remove_bike_light.click()
        time.sleep(3)
        
        remove_fleece_jacket = driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]')
        remove_fleece_jacket.click()
        time.sleep(3)
        
        try:
            driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
            sys.exit(1)
        except NoSuchElementException:
            pass
        
        add_tshirt = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        add_tshirt.click()
        time.sleep(3)
        
        cart_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert cart_badge.text == '1'
        
        sys.exit(0)
        
    except Exception as e:
        driver.save_screenshot('C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\test_scenario_failure.png')
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    test_ui_scenario()
