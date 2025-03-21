
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        )
        password_field = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')

        username_field.send_keys(username)
        time.sleep(3)
        password_field.send_keys(password)
        time.sleep(3)
        login_button.click()
        time.sleep(3)

def main():
    try:
        # Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument('--disable-features=NetworkService')

        # Initialize driver
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get('https://saucedemo.com/')
        
        # Wait for 5 seconds to let the page load
        time.sleep(5)

        # Execute login
        login_page = LoginPage(driver)
        login_page.login('standard_user', 'secret_sauce')

        # Add items to the cart
        bike_light = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        )
        fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')

        bike_light.click()
        time.sleep(3)
        fleece_jacket.click()
        time.sleep(3)

        # Check the cart count
        cart_count = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        )

        assert cart_count.text == '2', f"Expected cart count to be 2 but got {cart_count.text}"

        # Test passed, take screenshot and exit with code 0
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\test_case_passed.png")
        sys.exit(0)

    except Exception as e:
        # Test failed, take screenshot and exit with code 1
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\test_case_failed.png")
        print(f"Test failed due to exception: {e}")
        sys.exit(1)

    finally:
        # Close the driver
        driver.quit()

if __name__ == "__main__":
    main()
