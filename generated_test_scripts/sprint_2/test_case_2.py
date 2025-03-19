
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_add_to_cart():
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")

    # Initialize the driver
    driver = webdriver.Chrome(options=options)

    try:
        # Open the website and maximize window
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()

        # Login using LoginPage class method
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        # Adding wait before each action
        time.sleep(3)

        # Add 'Bike Light' to the cart
        bike_light = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        )
        bike_light.click()

        # Wait before next action
        time.sleep(3)

        # Add 'Fleece Jacket' to the cart
        fleece_jacket = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        )
        fleece_jacket.click()

        # Wait before next action
        time.sleep(3)

        # Verify the cart badge displays '2'
        cart_count = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        )
        assert cart_count.text == '2'

        # Capture the screenshot
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\cart_verification.png")

        # Test case passed
        sys.exit(0)

    except Exception as e:
        # Capture screenshot on failure
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\cart_verification_failed.png")
        # Print exception details
        print(f"Exception occurred: {e}")
        # Test case failed
        sys.exit(1)

    finally:
        # Close the driver
        driver.quit()

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_box = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        )
        password_box = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))
        )
        login_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="login-button"]'))
        )

        username_box.send_keys(username)
        time.sleep(3)

        password_box.send_keys(password)
        time.sleep(3)

        login_button.click()
        time.sleep(3)

if __name__ == "__main__":
    test_add_to_cart()
