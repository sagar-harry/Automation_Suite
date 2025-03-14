
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        )
        username_field.send_keys(username)
        
        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
        )
        password_field.send_keys(password)

        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]'))
        )
        login_button.click()

try:
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-features=NetworkService")

    # Initialize the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)

    # Maximize window and open the url
    driver.maximize_window()
    driver.get("https://saucedemo.com/")
    time.sleep(5)

    # Login to the application
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    time.sleep(3)

    # Add items to the cart
    bike_light_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
    )
    bike_light_button.click()
    time.sleep(3)

    fleece_jacket_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
    )
    fleece_jacket_button.click()
    time.sleep(3)

    # Verify the cart badge displays '2'
    cart_count = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
    )
    assert cart_count.text == '2', f"Expected cart count to be '2' but found {cart_count.text}"

    # Snapshot the page
    driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\cart_verification.png')

    sys.exit(0)

except Exception as e:
    driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\cart_verification_failure.png')
    print(f"Test failed due to: {e}")
    sys.exit(1)

finally:
    driver.quit()
