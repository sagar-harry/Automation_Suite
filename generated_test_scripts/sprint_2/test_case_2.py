
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def setup_browser():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://saucedemo.com/")
    time.sleep(5)  # Wait for 5 secs after the page is opened
    return driver

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        time.sleep(3)  # Wait before action
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        time.sleep(3)  # Wait before action
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(3)  # Wait before action

def test_cart_count():
    driver = setup_browser()
    try:
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)  # Wait before action
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)  # Wait before action

        cart_count_elem = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        cart_count = cart_count_elem.text

        assert cart_count == '2', f"Expected cart count to be '2', but got {cart_count}"
        exit(0)  # Test case passed

    except Exception as e:
        print(e)
        exit(1)  # Test case failed

    finally:
        driver.quit()

if __name__ == "__main__":
    test_cart_count()
