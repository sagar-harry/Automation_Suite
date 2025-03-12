
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        ).send_keys(username)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))
        ).send_keys(password)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]'))
        ).click()

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=NetworkService")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    return driver

def test_ui_scenario():
    driver = setup_driver()
    try:
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
        
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]'))).click()

        time.sleep(3)
        cart_count = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        )
        assert cart_count.text == '2', "Cart count is not 2 after adding items."

        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]'))).click()

        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]'))).click()

        time.sleep(3)
        assert not driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span'), "Cart count element exists after removing items."

        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()

        time.sleep(3)
        cart_count = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        )
        assert cart_count.text == '1', "Cart count is not 1 after adding Bolt T-Shirt."

        driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png')
        sys.exit(0)
        
    except Exception as e:
        driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot_fail.png')
        print(f"Test failed due to: {e}")
        sys.exit(1)
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_ui_scenario()
