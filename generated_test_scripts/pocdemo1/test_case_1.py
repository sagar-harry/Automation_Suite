
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

def test_ui():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--disable-features=NetworkService')

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("https://saucedemo.com/")
        driver.maximize_window()
        time.sleep(5)

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        )
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]'))
        )
        driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('somename')
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('lastname')
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys('123456')
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="continue"]').click()
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="finish"]').click()
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()
        time.sleep(3)

        sys.exit(0)
    
    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)
    
    finally:
        driver.quit()

if __name__ == "__main__":
    test_ui()
