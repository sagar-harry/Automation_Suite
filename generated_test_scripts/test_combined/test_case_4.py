
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        user_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='user-name']"))
        )
        user_field.send_keys(username)

        pwd_field = self.driver.find_element(By.XPATH, "//*[@id='password']")
        pwd_field.send_keys(password)

        login_button = self.driver.find_element(By.XPATH, "//*[@id='login-button']")
        login_button.click()

def test_ui():
    url = "https://saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"

    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=NetworkService")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        driver.get(url)
        time.sleep(5)
        driver.maximize_window()

        login_page = LoginPage(driver)
        login_page.login(username, password)
        time.sleep(3)

        bike_light_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']"))
        )
        bike_light_btn.click()
        time.sleep(3)

        fleece_jacket_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']"))
        )
        fleece_jacket_btn.click()
        time.sleep(3)

        cart_count = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='shopping_cart_container']/a/span"))
        )

        assert cart_count.text == '2', f"Expected cart count to be 2, but it was {cart_count.text}"
        sys.exit(0)

    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)
    
    finally:
        driver.save_screenshot("C:/Users/Administrator/Desktop/QE_COE/automated_pipeline_2/captured_screenshots/test_ui.png")
        driver.quit()

if __name__ == "__main__":
    test_ui()
