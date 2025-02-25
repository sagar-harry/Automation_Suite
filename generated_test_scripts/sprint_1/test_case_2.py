
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

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

def main():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)
    driver.get("https://saucedemo.com/")
    driver.maximize_window()
    time.sleep(5)

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('somename')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('lastname')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys('123456')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()
    time.sleep(3)

    try:
        payment_info = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]')
        if payment_info.is_displayed():
            print("Payment Information is visible. Test Case Passed.")
            sys.exit(0)
    except:
        print("Payment Information not visible. Test Case Failed.")
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
