
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
    def login(self, username, password):
        time.sleep(3)  # Wait for 3 secs before action
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').clear()
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').clear()
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()


def test_ui_cart_scenario():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(options=options) 

    try:
        driver.get("https://saucedemo.com/")
        time.sleep(5)  # Wait for 5 secs after page load
        driver.maximize_window()
        
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        
        time.sleep(3)  # Wait for 3 secs before action
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        
        time.sleep(3)  # Wait for 3 secs before action
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()

        time.sleep(3)  # Wait for 3 secs before action
        cart_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert cart_badge.text == '2', "Cart badge count not matching after adding two items"

        time.sleep(3)  # Wait for 3 secs before action
        driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]').click()
        driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bolt-t-shirt"]').click()

        cart_badge = driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert len(cart_badge) == 0, "Cart is not empty after reset"

        time.sleep(3)  # Wait for 3 secs before action
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()

        time.sleep(3)  # Wait for 3 secs before action
        cart_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert cart_badge.text == '1', "Cart badge count not matching after adding one item post-reset"

        exit(0)  # Exit with 0 if the test case passes
    except Exception as e:
        print(f"Test failed due to: {str(e)}")
        exit(1)  # Exit with 1 if the test case fails
    finally:
        driver.quit()

test_ui_cart_scenario()
