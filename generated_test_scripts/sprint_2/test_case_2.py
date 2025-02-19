
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_element = self.driver.find_element(By.XPATH, '//*[@id="user-name"]')
        password_element = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')

        username_element.send_keys(username)
        time.sleep(3)
        password_element.send_keys(password)
        time.sleep(3)
        login_button.click()
        time.sleep(3)

def main():
    try:
        options = Options()
        options.headless = True
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--incognito")

        driver = webdriver.Chrome(options=options)
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        bike_light = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        bike_light.click()
        time.sleep(3)

        fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        fleece_jacket.click()
        time.sleep(3)

        cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert cart_count.text == '2'
        
        driver.quit()
        exit(0)
    except Exception as e:
        print(str(e))
        exit(1)

if __name__ == "__main__":
    main()
