
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
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(3)

def test_ui():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=NetworkService")
    driver = webdriver.Chrome(options=options)

    driver.get('https://saucedemo.com/')
    driver.maximize_window()
    time.sleep(5)

    try:
        login_page = LoginPage(driver)
        login_page.login('standard_user', 'secret_sauce')

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]/a'))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout"]'))).click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="first-name"]'))).send_keys('Jonnathan')
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('K')
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys('10007')
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="continue"]').click()
        time.sleep(3)

        payment_info = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]'))
        )

        if payment_info.is_displayed():
            driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")
            sys.exit(0)
        else:
            sys.exit(1)

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    test_ui()
