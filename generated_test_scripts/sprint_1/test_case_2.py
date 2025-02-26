
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
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)
    driver.get("https://saucedemo.com/")
    driver.maximize_window()
    time.sleep(5)

    try:
        login_page = LoginPage(driver)
        
        # Log in
        login_page.login(username='standard_user', password='secret_sauce')
        time.sleep(3)

        # Add items to cart
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
        time.sleep(3)

        # Proceed to cart
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a'))).click()
        time.sleep(3)
        
        # Proceed to checkout
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="checkout"]'))).click()
        time.sleep(3)

        # Enter user details and continue
        driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('somename')
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('lastname')
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys('123456')
        time.sleep(3)
        
        driver.find_element(By.XPATH, '//*[@id="continue"]').click()
        time.sleep(3)

        # Verify payment information is visible
        payment_information_visible = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]')))
        
        if payment_information_visible:
            sys.exit(0)
        else:
            sys.exit(1)

    except Exception as e:
        print(e)
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
