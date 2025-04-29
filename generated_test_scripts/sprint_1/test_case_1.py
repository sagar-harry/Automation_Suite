
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(5)

def test_cart_functionality():
    options = Options()
    options.add_argument('--incognito')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-features=NetworkService')
    driver = webdriver.Chrome(options=options)

    try:
        driver.get('https://saucedemo.com/')
        time.sleep(5)
        driver.maximize_window()
        time.sleep(5)

        login_page = LoginPage(driver)
        login_page.login('standard_user', 'secret_sauce')

        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()

        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()

        time.sleep(3)
        cart_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert cart_badge.text == '2', f"Expected cart badge count to be '2', but was {cart_badge.text}"

        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]').click()

        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]').click()

        time.sleep(3)
        try:
            cart_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
            assert False, "Cart count element should not exist, but it does."
        except NoSuchElementException:
            pass  # This is expected

        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()

        time.sleep(3)
        cart_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert cart_badge.text == '1', f"Expected cart badge count to be '1', but was {cart_badge.text}"

        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")
        sys.exit(0)

    except Exception as e:
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\failed_screenshot.png")
        sys.exit(1)
    
    finally:
        driver.quit()

if __name__ == "__main__":
    test_cart_functionality()
