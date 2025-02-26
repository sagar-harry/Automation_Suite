
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
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

def main():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    url = "https://saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"

    try:
        driver.get(url)
        time.sleep(5)

        login_page = LoginPage(driver)
        login_page.login(username, password)
        
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()

        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()

        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()

        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="checkout"]').click()

        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("somename")
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("lastname")
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("123456")

        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="continue"]').click()

        time.sleep(3)
        payment_information_label = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]')

        if payment_information_label.is_displayed():
            print("Test Passed")
            sys.exit(0)
        else:
            print("Test Failed")
            sys.exit(1)

    except Exception as e:
        print(f"Test Failed: {str(e)}")
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
