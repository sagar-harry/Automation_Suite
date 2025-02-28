
import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        
    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))).send_keys(username)
        sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        sleep(3)

def test_checkout_payment_info_visibility():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument('--disable-features=NetworkService')
        
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://saucedemo.com/')
        driver.maximize_window()
        sleep(5)
        
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
        sleep(3)
        
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        sleep(3)
        
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        sleep(3)
        
        driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
        sleep(3)
        
        driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("Jonnathan")
        sleep(3)
        
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("K")
        sleep(3)
        
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("10007")
        sleep(3)
        
        driver.find_element(By.XPATH, '//*[@id="continue"]').click()
        sleep(3)
        
        payment_info_visible = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]'))
        )

        assert payment_info_visible is not None
        sys.exit(0)
    except Exception as e:
        sys.exit(1)
    finally:
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\checkout_test.png")
        driver.quit()

if __name__ == "__main__":
    test_checkout_payment_info_visibility()
