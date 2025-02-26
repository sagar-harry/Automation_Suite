
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

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

try:
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popups")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)

    driver.get("https://saucedemo.com/")
    time.sleep(5)
    driver.maximize_window()

    login_page = LoginPage(driver)
    login_page.login('standard_user', 'secret_sauce')

    bike_light_element = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
    time.sleep(3)
    bike_light_element.click()
    time.sleep(3)

    fleece_jacket_element = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
    time.sleep(3)
    fleece_jacket_element.click()
    time.sleep(3)

    cart_count_element = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    cart_count = cart_count_element.text

    screenshot_path = r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots'
    driver.save_screenshot(f'{screenshot_path}\\snapshot.png')

    driver.quit()

    assert cart_count == '2', f"Expected 2, but got {cart_count}"
    sys.exit(0)

except Exception as e:
    print(f"Test Failed: {e}")
    sys.exit(1)
