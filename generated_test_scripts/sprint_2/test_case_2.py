
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

def test_cart_count():
    options = Options()
    options.headless = True
    options.add_argument('--disable-notifications')
    options.add_argument('--incognito')

    driver = webdriver.Chrome(options=options)
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    driver.maximize_window()

    login_page = LoginPage(driver)
    login_page.login('standard_user', 'secret_sauce')

    wait = WebDriverWait(driver, 10)

    bike_light = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
    time.sleep(3)
    bike_light.click()

    fleece_jacket = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
    time.sleep(3)
    fleece_jacket.click()

    cart_count = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
    assert cart_count.text == '2', f"Expected cart count to be 2, but got {cart_count.text}"

    driver.quit()
    sys.exit(0)

try:
    test_cart_count()
except AssertionError as e:
    print(str(e))
    sys.exit(1)
